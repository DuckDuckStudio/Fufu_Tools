@echo off
chcp 65001

echo --- Python version ---
python --version

echo --- pip version ---
pip --version

echo --- System version ---
ver

echo --- System Bits ---
set TheBit=x%PROCESSOR_ARCHITECTURE:~-2%
echo  %TheBit%

echo --- Fufu Tools version ---
for /f "delims=[" %%i in (Version) do (
    echo %%i
)

echo --- Installed library files ---
pip list

echo --- Directory where Fufu Tools is located ---
echo %cd%

echo --- Network connection status ---
set url=www.baidu.com
ping -6 %url% >nul
if %errorlevel% equ 0 (
    echo Connection normal
    echo [INFO] Using IPv6 to check connect.
) else (
    echo Connect failed
    echo [INFO] Using IPv6 to check connect. If your device does not support IPv6, please check it yourself.
)

echo --- Github connection status ---
set url=www.github.com
ping %url% >nul
if %errorlevel% equ 0 (
    echo Connection normal
) else (
    echo Connect failed
)

echo --- limits of authority ---
net.exe session 1>NUL 2>NUL && (
    echo Administrator.
) || (
    echo Non administrator.
)

pause