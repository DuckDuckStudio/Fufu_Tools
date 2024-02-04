@echo off

rem 清空已存在的 INFO.txt 文件
echo. > "INFO.txt"

echo Checking...

echo --- Console used encoding --- >> "INFO.txt"
chcp >> "INFO.txt"

echo --- Python version --- >> "INFO.txt"
python --version >> "INFO.txt"

echo --- pip version --- >> "INFO.txt"
pip --version >> "INFO.txt"

echo --- System version --- >> "INFO.txt"
ver >> "INFO.txt"

echo --- System Bits --- >> "INFO.txt"
set TheBit=x%PROCESSOR_ARCHITECTURE:~-2%
echo  %TheBit% >> "INFO.txt"

echo --- Fufu Tools version --- >> "INFO.txt"
for /f "delims=[" %%i in (Version) do (
    echo %%i >> "INFO.txt"
)

echo --- Installed library files --- >> "INFO.txt"
pip list >> "INFO.txt"

echo --- Directory where Fufu Tools is located --- >> "INFO.txt"
echo %cd% >> "INFO.txt"

echo --- Network connection status --- >> "INFO.txt"
set url=www.baidu.com
ping -6 %url% >nul
if %errorlevel% equ 0 (
    echo Connection normal >> "INFO.txt"
    echo [INFO] Using IPv6. >> "INFO.txt"
) else (
    echo Connect failed >> "INFO.txt"
    echo [INFO] Using IPv6. >> "INFO.txt"
)
ping -4 %url% >nul
if %errorlevel% equ 0 (
    echo Connection normal >> "INFO.txt"
    echo [INFO] Using IPv4. >> "INFO.txt"
) else (
    echo Connect failed >> "INFO.txt"
    echo [INFO] Using IPv4. >> "INFO.txt"
)

echo --- Github connection status --- >> "INFO.txt"
set url=www.github.com
ping %url% >nul
if %errorlevel% equ 0 (
    echo Connection normal >> "INFO.txt"
) else (
    echo Connect failed >> "INFO.txt"
)

echo --- limits of authority --- >> "INFO.txt"
net.exe session 1>NUL 2>NUL && (
    echo Administrator. >> "INFO.txt"
) || (
    echo Non administrator. >> "INFO.txt"
)

echo The information has been saved to INFO.txt in the directory of the Fufu Tools.

pause
