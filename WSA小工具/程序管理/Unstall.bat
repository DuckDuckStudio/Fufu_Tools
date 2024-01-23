@echo off
chcp 65001
cls

echo 当前使用的ADB版本为：
adb version
:: Show ADB version

echo ---WSA 应用卸载程序---

:ct
adb connect 127.0.0.1:58526
:: Connect to WSA (try)

:pk
echo 设备已安装的全部包：
adb shell pm list packages
:: Into adb shell (ADB交互模式) & packname list (列出包名) & exit

echo ----------

echo 设备已安装的全部*第三方*包：
adb shell pm list packages -3
:: 列出除系统包外第三方包

echo ----------

set /p pack_name="请输入你要卸载的程序的包名:"
:: Get pack name (获取需要卸载的包名)

:: Right(?) code in here!
if /I %pack_name:~1%=="exit" (
    echo 了解，程序取消执行！
    goto :EOF
) else if /I %pack_name:~1%=="repk" (
    echo 了解，程序重新检查安装的包
    goto :pk
) else if /I %pack_name:~1%=="rect" (
    echo 了解，程序重新连接并检查安装的包
    goto :ct
) else (
    echo 正在卸载...

    adb shell pm uninstall %pack_name:~1%
    :: Uninstall this pack(app)

    echo 卸载完成！

    echo ---现在已安装的包有：---
    adb shell pm list packages

    echo ----------

    echo ---现已安装的第三方包有：---
    adb shell pm list packages -3
    :: Into adb shell (ADB交互模式) & packname list (列出包名) & exit
)

pause