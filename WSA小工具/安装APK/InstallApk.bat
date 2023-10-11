@echo off

REM using --GBK-- for this file.
REM Don't using other for this file !!!

REM ----------------ERROR--NOTES-----------------------
REM 在允许调试的情况下暂未出现问题
REM ----------------------------------------------------

REM Welcome
echo 欢迎使用APK安装程序(for WSA)

REM --Get apk's route--
set /p apk_route="请输入或粘贴您的APK文件所在的完整路径(例如D:\xxx.apk): "
echo 收到！请确保WSA启动并正确配置ADB(安卓调试桥)

REM ---using ADB to install APK---

adb kill-server
adb start-server
REM Open ADB server (重启确认)

REM connect WSA
adb connect 127.0.0.1:58526
REM --No checks--

REM ---Install APK---
adb install %apk_route%
REM 仅限只有一个连接时，else 必须 use `adb shell xxx`

REM --wait--

REM End
echo 安装完成！