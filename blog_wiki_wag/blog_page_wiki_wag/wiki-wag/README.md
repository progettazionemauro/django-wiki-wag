# wiki-wag
12/09/23 - Implementato hook:
#!/bin/bash

# Get the commit message as input
read -p "Enter the commit message: " commit_message

# Get the current branch name and assign it to the central_branch variable
central_branch=$(git rev-parse --abbrev-ref HEAD)

# Ask the user whether to create a new branch or remain on the current branch
read -p "Do you want to create a new branch? (y/n): " answer

if [[ $answer == "y" ]]; then
  # Get the name of the new branch from the user
  read -p "Enter the name of the new branch: " new_branch

  # Check if the local branch exists, if not, create it from the central branch
  if ! git show-ref --quiet refs/heads/$new_branch; then
    git checkout -b $new_branch $central_branch
  else
    git checkout $new_branch
  fi

  # Get the commit message for the new changes
  read -p "Enter the commit message for the new changes: " new_commit_message

  # Commit the changes on the new branch
  git add .
  git commit -m "$new_commit_message"

  # Push changes to the new local branch
  echo "Pushing changes to $new_branch"
  git push origin $new_branch

  # Switch to the new branch on the DigitalOcean droplet
  echo "Switching to the new branch on the Hetzener Cloud..."
  ssh root@65.108.158.205 "cd /home/wiki-wag/quintiliano && git checkout $new_branch"
else
  # Commit the changes on the current branch
  git add .
  git commit -m "$commit_message"

  # Push changes to the current branch
  echo "Pushing changes to the current branch"
  git push origin $(git rev-parse --abbrev-ref HEAD)

  # Switch to the branch on the Hetzener Cloud
  echo "Switching to the current branch on the DigitalOcean droplet..."
  ssh root@65.108.158.205 "cd /home/wiki-wag/quintiliano && git checkout $(git rev-parse --abbrev-ref HEAD)"
fi

# Pull changes from the remote central branch on GitHub
echo "Pulling changes from origin/$central_branch"
git fetch origin
git reset --hard origin/$central_branch

# al 16/9/23 - costrutito sistema ssh 
# The error message suggests that the SSH key file /root/.ssh/id_rsa_hetzner_github does not exist at the specified 
# location. Make sure that the file is in the correct directory and that the file name is spelled correctly

Tolta passphrase

14/09/23 - Modifica degli ssh

# Check if there are any conflicts after pulling
if [ $? -eq 0 ]; then
  # No conflicts, proceed with the push
  # Push changes to the GitHub repository
  echo "Pushing changes to origin/$central_branch"
  git push origin $central_branch

  # Log in to the DigitalOcean droplet and pull the changes
  echo "Logging in to the Hetzener Cloud..."
  ssh root@65.108.158.205 "cd /home/wiki-wag/quintiliano && git pull"

  echo "Changes successfully pushed to both GitHub and the Hetzener Cloud."
else
  # Conflicts exist, prompt the user to resolve them manually
  echo "There are conflicts after pulling. Please resolve the conflicts manually and commit the changes."
fi

Sembra che non funzioni

23/9/23 - h. 8:36 miglioramento branch delete

23/9/23 - Processo streamline consolidato con git hooks delete e update
23/09/23 - Implementazione di blocco <pre> <code>
25/09/23 - Consolidato il flusso di raw html - Cambiamento per gli unstahed - Prova dello script senza stahes