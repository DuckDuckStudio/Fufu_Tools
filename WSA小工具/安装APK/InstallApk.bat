@echo off

REM using --GBK-- for this file.
REM Don't using other for this file !!!

REM ----------------ERROR--NOTES-----------------------
REM ��������Ե��������δ��������
REM ----------------------------------------------------

REM Welcome
echo ��ӭʹ��APK��װ����(for WSA)

REM --Get apk's route--
set /p apk_route="�������ճ������APK�ļ����ڵ�����·��(����D:\xxx.apk): "
echo �յ�����ȷ��WSA��������ȷ����ADB(��׿������)

REM ---using ADB to install APK---

adb kill-server
adb start-server
REM Open ADB server (����ȷ��)

REM connect WSA
adb connect 127.0.0.1:58526
REM --No checks--

REM ---Install APK---
adb install %apk_route%
REM ����ֻ��һ������ʱ��else ���� use `adb shell xxx`

REM --wait--

REM End
echo ��װ��ɣ�