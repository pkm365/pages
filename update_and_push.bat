@echo off
chcp 65001
echo Updating navigation page...
python generate_nav.py

echo Adding changes to Git...
git add .

echo Committing changes...
set /p commit_msg=Enter commit message (press Enter for default message): 
if "%commit_msg%"=="" (
    git commit -m "Update navigation and content"
) else (
    git commit -m "%commit_msg%"
)

echo Pushing to GitHub...
git push origin main

echo Done!
pause 