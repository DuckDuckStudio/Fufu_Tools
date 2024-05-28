# 计时程序开启时间显示提示
# 默认随主程序开启 -> 自启动？
# 隐藏控制台 (pyw)

# 导入
from plyer import notification
import time
import configparser
import os
import sys

# READ config.ini file
script_dir = os.path.dirname(sys.argv[0])
config_file_path = os.path.join(script_dir, "config.ini")
config = configparser.ConfigParser()
config.read(config_file_path)
total_seconds = config.getint('set', 'time_s')

# 转换至h
time_min = 0
time_hour = total_seconds / 60 / 60
if time_hour < 1:
    time_min = total_seconds / 60

if time_min:
    text = time_min, "分钟"
else:
    text = time_hour, "小时"

while total_seconds >= 0:
    time.sleep(1)
    total_seconds -= 1

# at end time
notification.notify(
    title='休息一下吧！',
    message=f'已经使用设备超过 {text[0]} {text[1]} 了，休息一下吧！\n',
    timeout=10
)

# No more down ...
