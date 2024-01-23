@echo off
chcp 65001
cls

echo 感谢你使用本程序
set /p file_route="请输入你要查找的目录(不用引号): "
set /p file_format="请输入你要查找的文件类型(例如mp4): "

cd /d "%~dp0" 

type nul >%cd%\查找结果.txt
for /r "%file_route%" %%a in (*.%file_format%) do (
    >>%cd%\查找结果.txt echo %%~dpa%%~nxa
)

echo 程序运行结束，请查看程序所在目录下生成的文件！

pause