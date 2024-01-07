#!/bin/bash

read -p "Enter the commit message: " commit_message
central_branch=$(git rev-parse --abbrev-ref HEAD)

read -p "Do you want to create a new branch? (y/n): " answer

if [[ $answer == "y" ]]; then
  read -p "Enter the name of the new branch: " new_branch
  git checkout -B $new_branch $central_branch
fi

# Add and commit local changes
git add .
git commit -m "$commit_message"

current_branch=$(git rev-parse --abbrev-ref HEAD)

# Pull the latest changes from the remote branch and rebase them
git pull origin $current_branch --rebase

if [ $? -eq 0 ]; then
  # If there is no conflict, push the changes to the remote branch
  echo "Pushing changes to $current_branch"
  git push origin $current_branch
  
  # Update the Hetzner Cloud
  echo "Updating the branch on the Hetzner Cloud..."
  ssh root@65.108.158.205 "cd /home/wiki-wag/quintiliano && git checkout $current_branch && git pull origin $current_branch"
  echo "Changes successfully pushed to both GitHub and the Hetzner Cloud."
else
  echo "There are conflicts after pulling and rebasing. Please resolve the conflicts manually and commit the changes."
fi
