@echo off
chcp 65001
cls

echo 正在删除缓存文件...

del /s /q "%temp%\*.*"
del /s /q "C:\Documents and Settings\%USERNAME%\Local Settings\temp\*.*"
del /s /q "%tmp%\*.*"

echo 缓存文件删除完成！按任意键退出！

pause
