@echo on

REM 检测Python是否已安装
python --version > nul 2>&1

IF %ERRORLEVEL% NEQ 0 (
    REM Python未安装，执行安装操作
    echo 正在安装Python，请稍等...

    REM 使用winget安装Python（示例使用的是Python 3.9）
    :: winget install -e --id Python.Python.3 -h
    
    REM 检测安装是否成功
    ::python --version > nul 2>&1
    
    ::IF %ERRORLEVEL% EQU 0 (
    ::    REM 安装成功
    ::    echo 已安装Python
    ::) ELSE (
    ::    REM 安装失败
    ::    echo Python安装失败，请手动安装
    ::)
) ELSE (
    REM Python已安装
    echo 恭喜你，你已经安装了Python
)

pause