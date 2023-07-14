@echo off
set /p folder="请输入要删除的文件夹路径(不要包含引号)："
takeown /f "%folder%" /r /d y
icacls "%folder%" /grant administrators:F /t
rd /s /q "%folder%"
echo 删除完成！
pause
