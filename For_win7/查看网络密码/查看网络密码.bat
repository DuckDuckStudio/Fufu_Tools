@echo off
echo "��ǰ�������ӹ���wifi:"
netsh wlan show profiles
:main
set /p wifi_name="��������Ҫ��ѯ��wifi��:"
netsh wlan show profile name="%wifi_name%" key=clear
echo,
echo "�㻹���ѯ����wifi��?��y/n��"

set /p input="�����벢ѡ��:"
if %input%==y goto main
REM Y
if %input%==n pause
REM N