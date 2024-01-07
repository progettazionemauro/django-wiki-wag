#!/bin/bash

# Address of the Hetzner Server
HETZNER_ADDRESS="65.108.158.205"
# Directory on Hetzner Server where the Git repository is located
HETZNER_DIR="/home/wiki-wag/quintiliano"

# Verify the integrity of the Git repository
echo "Checking repository integrity..."
# `git fsck` checks the integrity of the repository and reports any problems
if git fsck; then
  echo "Repository is intact."
else
  echo "Repository has integrity issues. Exiting."
  exit 1
fi

# Perform garbage collection to remove dangling objects
echo "Cleaning up repository..."
# `git gc --prune=now` removes objects not pointed to by any commit
git gc --prune=now

# Get the name of the current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)
central_branch="$current_branch"

# If the current branch has integrity issues, attempt to switch to the chronologically previous branch
if [[ "$(git fsck --no-reflog | grep '^(bad)')" ]]; then
  echo "Current branch $current_branch has integrity issues."
  # Find the most recent branch, which is not the current one
  alternate_branch=$(git for-each-ref --sort=-committerdate --format='%(refname:short)' refs/heads | grep -v "$current_branch" | head -n 1)
  if [[ -n $alternate_branch ]]; then
    echo "Switching to $alternate_branch before performing operations on $current_branch."
    git checkout $alternate_branch || exit 1
  else
    echo "No suitable alternate branch available. Exiting."
    exit 1
  fi
fi

# Initialize an array to store the names of branches that can be deleted
branches=()

# Iterate over each branch in the local repository
while IFS= read -r branch; do
  if [[ "$branch" != "$current_branch" && $(git merge-base $branch $current_branch) == $(git rev-parse $branch) ]]; then
    last_modified=$(git log -1 --format=%cd --date=format:'%d-%m-%Y %H:%M:%S' $branch)
    branches+=("$branch ($last_modified)")
  fi
done < <(git branch)

# If there are no branches to delete, exit the script
if [[ ${#branches[@]} -eq 0 ]]; then
  echo "No branches to delete."
  exit 0
fi

# List the branches that can be deleted
echo "Branches that can be deleted:"
for ((i=0; i<${#branches[@]}; i++)); do
  echo "$(($i+1)). ${branches[i]}"
done

# Prompt the user to enter the number corresponding to the branch they want to delete
read -p "Enter the number of the branch to delete: " branch_number
if [[ $branch_number -lt 1 || $branch_number -gt ${#branches[@]} ]]; then
  echo "Invalid number."
  exit 1
fi

# Extract the branch name from the branches array using the entered number
branch_to_delete=$(echo "${branches[$(($branch_number-1))]}" | awk -F' \\(' '{print $1}')

# Confirm the branch to delete
echo "Branch to Delete: $branch_to_delete"

# If the branch to delete is the current branch, switch to the most recent branch before deletion
if [[ "$branch_to_delete" == "$current_branch" ]]; then
  alternate_branch=$(git for-each-ref --sort=-committerdate --format='%(refname:short)' refs/heads | grep -v "$branch_to_delete" | head -n 1)
  echo "Switching to $alternate_branch before deleting $branch_to_delete."
  git checkout $alternate_branch || exit 1
fi

# Delete the branch locally
git branch -d $branch_to_delete

# Delete the branch from the central (GitHub) and Hetzner server if they exist there
# If the branch exists on the remote (GitHub in this case), delete it
if git ls-remote --heads origin $branch_to_delete > /dev/null; then
  # This command checks if the branch exists in the remote repository.
  # 'git ls-remote' command lists all references in a remote repository
  # '--heads' option restricts the listing to branch heads only
  # 'origin' refers to the default name of the remote repository
  # '$branch_to_delete' is the name of the branch to be deleted
  # '> /dev/null' suppresses the command output
  git push origin --delete $branch_to_delete
fi

# If the branch exists on the Hetzner server, delete it
if ssh root@$HETZNER_ADDRESS "cd $HETZNER_DIR && git show-ref --quiet refs/heads/$branch_to_delete"; then
 # Execute a command on the Hetzner server to delete the branch
  ssh root@$HETZNER_ADDRESS "cd $HETZNER_DIR && git branch -d $branch_to_delete"
fi

# Sync the central branch with the origin and Hetzner server
echo "Syncing with origin/$central_branch"
git pull origin $central_branch && git push origin $central_branch
if [ $? -eq 0 ]; then
 # If the sync is successful, pull the changes to the Hetzner server
  ssh root@$HETZNER_ADDRESS "cd $HETZNER_DIR && git pull"
  echo "Sync successful."
else
 # If there are conflicts during the sync, prompt the user to resolve them manually
  echo "Resolve conflicts manually."
fi
