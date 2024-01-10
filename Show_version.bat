@echo off
chcp 65001
cls

for /f "delims=[" %%i in (Version) do (
    echo %%i
)

pause