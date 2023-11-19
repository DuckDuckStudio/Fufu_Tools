@echo off

for /f "delims=[" %%i in (Version) do (
    echo %%i
)

echo 按任意键退出
pause >nul