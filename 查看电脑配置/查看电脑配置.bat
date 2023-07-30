@echo off
chcp 65001
REM 使用UTF-8编码
REM 显示设备信息
echo "您的设备信息如下："
REM 默认英文版本
systeminfo
echo " Tips:默认为英文版本，如需查看中文版本，请打开新的cmd窗口并键入“systeminfo” "