@echo off
chcp 65001
cls

adb kill-server
:: close the ADB

timeout /t 2
:: Sleep to wait

adb start-server
:: Open the ADB agin

echo 重启完成
:: Show tip

REM ---END---