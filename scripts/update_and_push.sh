#!/bin/bash

echo "Pulling latest changes from GitHub..."
git pull origin main

echo "Updating navigation page..."
python3 scripts/generate_nav.py

echo "Adding changes to Git..."
git add .

echo "Committing changes..."
read -p "Enter commit message (press Enter for default message): " commit_msg
if [ -z "$commit_msg" ]; then
    git commit -m "Update navigation and content - 榆林创新院成果超市看板转换完成"
else
    git commit -m "$commit_msg"
fi

echo "Pushing to GitHub..."
git push origin main

echo "Done!"