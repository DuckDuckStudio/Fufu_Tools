@echo off
REM 关闭回显
chcp 65001
REM 使用UTF-8编码
REM 初始化完毕

:set_name
set /p file_name="请输入你要生成的文件名(不要加后缀名):"
REM 获取%file_name%(生成文件名)
echo 好的~接下来...

set /p file_format="请输入你要生成的文件的格式(例如.exe):"
REM 获取%file_format%(生成文件格式)
echo 好的~接下来...

set /p file_size="请输入你要生成的文件的大小(以B为单位):"
REM 获取%file_size%(生成文件大小)
echo 好的~接下来...

set /p file_route="请输入你要生成文件的路径(例如D:\):"
REM 获取%file_route%(生成文件路径)
echo 需求条件已全部收集完毕！接下来...

echo 文件正在生成...
REM 生成文件
set file_complete_name=%file_name%%file_format%
set file_complete_route=%file_route%%file_complete_name%

fsutil file createnew  %file_complete_route% %file_size%

REM 判断文件是否正确生成
if exist %file_complete_route% (
    echo 恭喜你，文件生成成功！
) else (
    echo 很抱歉，文件生成失败，你可以尝试重新启动本程序。
    echo 当然，如果你知道具体问题或者能提供配置的，你可以提交【Issues】
)

echo 程序运行完毕！将在3秒后自动退出！
timeout /t 3

exit
REM 结束