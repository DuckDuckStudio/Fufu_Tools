@echo off

echo ��л��ʹ�ñ�����
set /p file_route="��������Ҫ���ҵ�Ŀ¼(��������): "
set /p file_format="��������Ҫ���ҵ��ļ�����(����mp4): "

cd /d "%~dp0" ::������������λ��

type nul >%cd%\���ҽ��.txt
for /r "%file_route%" %%a in (*.%file_format%) do (
    >>%cd%\���ҽ��.txt echo %%~dpa%%~nxa
)

echo �������н�������鿴��������Ŀ¼�����ɵ��ļ���

pause