@echo off
REM �رջ���

echo ��л��ʹ�ñ�����
echo (�������������ͬ���Ƶ��ļ������޸�ʽ)
set /p file_route="��������Ҫ���ҵ�Ŀ¼(��������): "
set /p file_name="��������Ҫ�����ļ�������: "

cd /d "%~dp0" ::������������λ��

type nul >%cd%\���ҽ��.txt
for /r "%file_route%" %%a in (%file_name%.*) do (
    >>%cd%\���ҽ��.txt echo %%~dpa%%~nxa
)

echo �������н�������鿴��������Ŀ¼�����ɵ��ļ���

pause