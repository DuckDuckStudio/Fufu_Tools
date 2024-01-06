@echo off
REM 关闭回显

echo 感谢你使用本程序
echo (本程序仅查找相同名称的文件，不限格式)
set /p file_route="请输入你要查找的目录(不用引号): "
set /p file_name="请输入你要查找文件的名称: "

cd /d "%~dp0" ::避免意外的输出位置

type nul >%cd%\查找结果.txt
for /r "%file_route%" %%a in (%file_name%.*) do (
    >>%cd%\查找结果.txt echo %%~dpa%%~nxa
)

echo 程序运行结束，请查看程序所在目录下生成的文件！

pause