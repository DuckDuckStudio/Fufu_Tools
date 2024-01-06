@echo off
chcp 65001
REM 使用UTF-8编码
echo "当前电脑连接过的wifi:"
netsh wlan show profiles
:main
set /p wifi_name="请输入你要查询的wifi名:"
netsh wlan show profile name="%wifi_name%" key=clear
echo,
echo "你还想查询其他wifi吗?（y/n）"

set /p input="请输入并选择:"
if %input%==y goto main
REM Y
if %input%==n pause
REM N