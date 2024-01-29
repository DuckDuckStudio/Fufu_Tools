@echo off
echo 尝试更新pip...
echo -------------------
python.exe -m pip install --upgrade pip
更新结束
echo -------------------
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
echo 正在安装库 ntplib
pip install ntplib
echo 安装库 ntplib 结束
echo -------------------
echo 正在安装库 tqdm
pip install tqdm
echo 安装库 tqdm 结束
echo -------------------
echo 所有所需库文件安装完成！
echo 如有问题你可以将完整输出及你遇到的问题一起提交Issues！
echo 错误关键词ERROR，如有看到请确认库文件安装情况。
echo 如果看不懂可以使用翻译软件！
pause
