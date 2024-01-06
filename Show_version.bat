@echo off
chcp 65001
REM "cls" is del for dev program.

for /f "delims=[" %%i in (Version) do (
    echo %%i
)

pause