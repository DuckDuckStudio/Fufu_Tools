@echo off

echo ��ǰʹ�õ�ADB�汾Ϊ��
adb version
:: Show ADB version

echo ---WSA Ӧ��ж�س���---

:ct
adb connect 127.0.0.1:58526
:: Connect to WSA (try)

:pk
echo �豸�Ѱ�װ��ȫ������
adb shell pm list packages
:: Into adb shell (ADB����ģʽ) & packname list (�г�����) & exit

echo ----------

echo �豸�Ѱ�װ��ȫ��*������*����
adb shell pm list packages -3
:: �г���ϵͳ�����������

echo ----------

set /p pack_name="��������Ҫж�صĳ���İ���:"
:: Get pack name (��ȡ��Ҫж�صİ���)

:: Right(?) code in here!
if /I %pack_name:~1%=="exit" (
    echo �˽⣬����ȡ��ִ�У�
    goto :EOF
) else if /I %pack_name:~1%=="repk" (
    echo �˽⣬�������¼�鰲װ�İ�
    goto :pk
) else if /I %pack_name:~1%=="rect" (
    echo �˽⣬�����������Ӳ���鰲װ�İ�
    goto :ct
) else (
    echo ����ж��...

    adb shell pm uninstall %pack_name:~1%
    :: Uninstall this pack(app)

    echo ж����ɣ�

    echo ---�����Ѱ�װ�İ��У�---
    adb shell pm list packages

    echo ----------

    echo ---���Ѱ�װ�ĵ��������У�---
    adb shell pm list packages -3
    :: Into adb shell (ADB����ģʽ) & packname list (�г�����) & exit
)

pause