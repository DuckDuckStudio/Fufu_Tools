@echo off
set /p folder="请输入要删除的文件夹路径(不要包含引号)："
set cscs = 0
:start
takeown /f "%folder%" /r /d y
icacls "%folder%" /grant administrators:F /t
rd /s /q "%folder%"
if exist "%folder%" (
    if %cscs% < 5 (
        echo "检测到文件夹删除失败，正在重新尝试"
        set %cscs% += 1
        goto :start
    ) else (
        echo "重试次数过多，删除失败"
    )
) else (
    echo "删除完成"
)
pause
