@echo off
chcp 65001
REM 使用UTF-8编码
set /p folder="请输入要删除的文件夹路径(不要包含引号)："
:start
takeown /f "%folder%" /r /d y
icacls "%folder%" /grant administrators:F /t
rd /s /q "%folder%"
REM 检查文件夹是否任然存在
if exist "%folder%" (
    echo "检测到文件夹删除失败，正在重新尝试"
    goto :start
    REM 跳转到标签start
) else (
    echo "删除完成"
)
pause
