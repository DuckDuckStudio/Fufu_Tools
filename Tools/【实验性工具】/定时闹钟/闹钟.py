import os
import time
from datetime import datetime, timedelta
from pygame import mixer

os.system("cls") #去除pygame的社区输出

def print_progress_bar(percentage):
    """打印进度条"""
    bar_length = 50  # 进度条的长度
    block = int(round(bar_length * percentage))
    text = "\r进度: [{0}] {1}%".format("#" * block + "-" * (bar_length - block), round(percentage * 100, 2))
    print(text, end='')

user_input = input("请输入提醒时间（例如，15:30或15：30表示今天的15点30分）: ").replace('：', ':')
hour, minute = map(int, user_input.split(':'))

now = datetime.now()
target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
if target_time < now:
    target_time += timedelta(days=1)

# 计算初始时间差
total_seconds = (target_time - now).total_seconds()

ringtone_dir = './铃声文件'
files = os.listdir(ringtone_dir)
mp3_files = [file for file in files if file.endswith('.mp3')]

if len(mp3_files) == 1:
    ringtone_path = os.path.join(ringtone_dir, mp3_files[0])
    print(f"提醒将在 {target_time.strftime('%Y-%m-%d %H:%M')} 触发。")

    while True:
        now = datetime.now()
        elapsed_seconds = (now - (target_time - timedelta(seconds=total_seconds))).total_seconds()
        percentage = min(elapsed_seconds / total_seconds, 1.0)  # 限制百分比为最大值为1.0
        print_progress_bar(percentage)

        if now >= target_time:
            print("\n时间到了！正在播放铃声...")
            mixer.init()
            mixer.music.load(ringtone_path)
            mixer.music.play(-1)
            input("按任意键停止铃声...\n")
            mixer.music.stop()
            break

        time.sleep(1)  # 每1秒更新一次进度条
else:
    print("未找到铃声文件或铃声文件不唯一。")

input("按Enter键继续...")