@echo off

REM CODING:GBK --ps1 using--
REM bat file / Powershell code (ha?)

echo --本代码使用Powershell--
echo 注意：在下载无法直接下载的文件(例如xx网盘)时可能会无法下载！

set /p file_route="请输入你需要将文件下载到哪个文件夹："
cd /d %file_route%
 
set /p exename="请输入你需要将下载后的文件命名为什么："
set /p downurl="请输入文件下载链接："
:: 使用powershell附带的curl命令
powershell curl -o "%exename%" "%downurl%"

echo 下载完成！

pause