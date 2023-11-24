@echo off
REM 关闭回显
REM 删除临时文件夹
chcp 65001
REM 使用UTF-8编码
echo "正在删除缓存文件"
rd /s /q C:\Users\%USERNAME%\AppData\Local\Temp\*.*
rd /s /q C:\Documents and Settings\%USERNAME%\Local Settings\temp\*.*
rd /s /q C:\Windows\Temp\*.*

REM 创建新的临时文件夹
if exist D:\Temp (
    echo "C盘外已存在同名缓存文件夹，跳过缓存位置调整"
) else (
    echo "正在创建新的缓存文件夹"
    md D:\Temp

    REM 设置环境变量
    setx TEMP D:\Temp
    setx TMP D:\Temp
)

echo 程序运行完毕

REM 十分简洁(^▽^)
pause>nul
