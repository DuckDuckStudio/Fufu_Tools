@echo off
chcp 65001
cls

echo 尝试更新pip...
echo -------------------
python.exe -m pip install --upgrade pip
echo 更新结束
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
echo 正在安装库 piexif
pip install piexif
echo 安装库 piexif 结束
echo -------------------
echo 正在安装库 pyautogui
pip install pyautogui
echo 安装库 pyautogui 结束
echo -------------------
echo 正在安装库 keyboard
pip install keyboard
echo 安装库 keyboard 结束
echo -------------------
echo 所有所需库文件安装完成！
echo 错误关键词ERROR，如有看到请确认库文件安装情况。
echo 如果看不懂可以使用翻译软件！
pause
