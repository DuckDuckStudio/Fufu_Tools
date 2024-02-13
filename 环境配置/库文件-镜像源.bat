@echo off
chcp 65001
cls

REM 使用清华大学镜像源
REM url: https://pypi.tuna.tsinghua.edu.cn/simple

echo 尝试更新pip...
echo -------------------
python.exe -m pip install --upgrade pip --index-url https://pypi.tuna.tsinghua.edu.cn/simple
echo 更新结束
echo -------------------
echo 开始安装库文件...
REM ---
echo -------------------
echo 正在安装库 translate
pip install translate -i https://pypi.tuna.tsinghua.edu.cn/simple
echo 安装库 translate 结束
echo -------------------
echo 正在安装库 requests
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
echo 安装库 requests 结束
echo -------------------
echo 正在安装库 beautifulsoup4
pip install beautifulsoup4 -i https://pypi.tuna.tsinghua.edu.cn/simple
echo 安装库 beautifulsoup4 结束
REM skip to install "requests"
echo -------------------
echo 正在安装库 webbrowser
pip install webbrowser -i https://pypi.tuna.tsinghua.edu.cn/simple
echo 安装库 webbrowser 结束
REM skip to install "webbrowser"
echo -------------------
echo 正在安装库 ntplib
pip install ntplib -i https://pypi.tuna.tsinghua.edu.cn/simple
echo 安装库 ntplib 结束
echo -------------------
echo 正在安装库 tqdm
pip install tqdm -i https://pypi.tuna.tsinghua.edu.cn/simple
echo 安装库 tqdm 结束
echo -------------------
echo 正在安装库 piexif
pip install piexif -i https://pypi.tuna.tsinghua.edu.cn/simple
echo 安装库 piexif 结束
echo -------------------
echo 所有所需库文件安装完成！
echo 错误关键词ERROR，如有看到请确认库文件安装情况。
echo 如果看不懂可以使用翻译软件！
pause
