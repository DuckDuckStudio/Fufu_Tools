@echo off
chcp 65001
REM 使用UTF-8编码
set /p folder="请输入要删除的文件夹路径(不要包含引号)："
set cscs = 0
REM 初始化重试次数
:start
takeown /f "%folder%" /r /d y
icacls "%folder%" /grant administrators:F /t
rd /s /q "%folder%"
REM 检查文件夹是否任然存在
if exist "%folder%" (
    if %cscs% < 5 (
        echo "检测到文件夹删除失败，正在重新尝试"
        set %cscs% += 1
        REM 测试次数+1
        goto :start
        REM 跳转到标签start
    ) else (
        echo "重试次数过多，删除失败"
    )
) else (
    echo "删除完成"
)
pause
REM 无法测试删除失败的情况，如有问题请[提交Issues](https://github.com/DuckDuckStudio/Windows_Optimization_Widget/issues)
