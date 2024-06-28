import os
import sys
import time
import math
import configparser
from plyer import notification

# READ config.ini file
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
config_file_path = os.path.join(script_dir, "config.ini")
config = configparser.ConfigParser()
config.read(config_file_path)
total_seconds = config.getint('set', 'time_s')

if total_seconds <= 0:
    print(f"✕ 设置的时间必须为正整数")
    sys.exit(1)
# 转单位
# int 与 整除(//) 都是向0取整

if total_seconds >= 3600:
    if total_seconds % 3600 == 0:
        time_h = total_seconds // 3600
        text = f"{time_h} 小时"
    elif total_seconds % 1800 == 0:
        time_h = (total_seconds - 1800) // 3600 # 计算一共几个完整小时
        text = f"{time_h}个半 小时"
    elif total_seconds % 60 == 0:
        time_h = total_seconds // 3600
        time_m = (total_seconds % 3600) // 60
        text = f"{time_h}小时 {time_m}分钟"
    elif total_seconds % 3600 >= 60:
        time_h = total_seconds // 3600
        time_m = (total_seconds % 3600) // 60
        time_s = total_seconds % 60
        text = f"{time_h}小时 {time_m}分钟 {time_s}秒"
    else:
        time_h = total_seconds // 3600
        time_s = total_seconds % 3600
        text = f"{time_h}小时 {time_s}秒"
elif total_seconds == 1800:
    text = "半小时"
elif total_seconds >= 60:
    if total_seconds % 60 == 0:
        text = f"{total_seconds // 60} 分钟"
    else:
        time_s = total_seconds % 60
        text = f"{total_seconds // 60} 分钟 {time_s} 秒"
else:
    text = f"{total_seconds} 秒"

while total_seconds >= 0:
    time.sleep(1)
    total_seconds -= 1

# at end time
notification.notify(
    title='休息一下吧！',
    message=f'已经使用设备超过 {text} 了，休息一下吧！\n',
    timeout=10
)
