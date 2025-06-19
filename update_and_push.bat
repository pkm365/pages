@echo off
echo 正在更新导航页...
python generate_nav.py

echo 添加更改到Git...
git add .

echo 提交更改...
set /p commit_msg=请输入提交信息（直接回车使用默认消息）: 
if "%commit_msg%"=="" (
    git commit -m "Update navigation and content"
) else (
    git commit -m "%commit_msg%"
)

echo 推送到GitHub...
git push origin main

echo 完成！
pause 