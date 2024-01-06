@echo off
echo 如果你在执行本程序时遇到问题，请先检查网络连接与python安装情况。
echo 切记配置系统PATH路径！
echo 开始安装库文件...
REM ---
echo -------------------
echo 正在安装库 translate
pip install translate
echo 安装库 translate 结束
echo -------------------
echo 正在安装库 requests
pip install requests
echo 安装库 requests 结束
echo -------------------
echo 正在安装库 beautifulsoup4
pip install beautifulsoup4
echo 安装库 beautifulsoup4 结束
REM skip to install "requests"
echo -------------------
echo 正在安装库 webbrowser
pip install webbrowser
echo 安装库 webbrowser 结束
REM skip to install "webbrowser"
echo -------------------
echo 正在安装库 tkinter
pip install tkinter
echo 安装库 tkinter 结束
REM This is a standard storehouse
echo -------------------
echo 正在安装库 ntplib
pip install ntplib
echo 安装库 ntplib 结束
echo -------------------
echo 所有所需库文件安装完成！
echo 如有问题你可以将完整输出及你遇到的问题一起提交Issues！
pause
