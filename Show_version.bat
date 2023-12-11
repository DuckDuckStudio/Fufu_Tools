@echo off

for /f "delims=[" %%i in (Version) do (
    echo %%i
)

pause
