@echo off
set /p folder="������Ҫɾ�����ļ���·��(��Ҫ��������)��"
set cscs = 0
:start
takeown /f "%folder%" /r /d y
icacls "%folder%" /grant administrators:F /t
rd /s /q "%folder%"
if exist "%folder%" (
    if %cscs% < 5 (
        echo "��⵽�ļ���ɾ��ʧ�ܣ��������³���"
        set %cscs% += 1
        goto :start
    ) else (
        echo "���Դ������࣬ɾ��ʧ��"
    )
) else (
    echo "ɾ�����"
)
pause
