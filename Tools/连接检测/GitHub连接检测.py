import requests
from plyer import notification
import time
import os
import sys
from datetime import datetime
import configparser

# READ config.ini file
script_dir = os.path.dirname(sys.argv[0])
config_file_path = os.path.join(script_dir, "config.ini")
config = configparser.ConfigParser()
config.read(config_file_path)
wait = config.getint('time', 'wait-github')
translation = config.getboolean('Translation', 'Error-message')

def check_wlan():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get("https://www.github.com/", headers=headers)

    if translation:
        try:
            if response.status_code == 200:
                print("连接成功!")
                notification.notify(
                    title='GitHub连接状态',
                    message='您的计算机可以连接到GitHub啦！',
                    timeout=10
                )
                return True # 连接成功返回True
            else:
                print("连接失败！状态代码:", response.status_code)
                return False # 连接失败返回False
        except requests.exceptions.Timeout:
            print("连接超时！")
            return False # 连接超时返回False
        except requests.exceptions.ConnectionError:
            print("无法连接到远程服务器！")
            return False # 无法连接到远程服务器返回False
        except Exception as e:
            print("连接失败！")
            print("错误代码:", e)
            return False # 其他连接错误返回False
    else:
        try:
            if response.status_code == 200:
                print("连接成功!")
                notification.notify(
                    title='GitHub连接状态',
                    message='您的计算机可以连接到GitHub啦！',
                    timeout=10
                )
                return True # 连接成功返回True
            else:
                print("连接失败！状态代码:", response.status_code)
                return False # 连接失败返回False
        except Exception as e:
            print("连接失败！")
            print("错误代码:", e)
            return False # 其他连接错误返回False


#---

count = 0

while True:
    count += 1

    print("正在尝试连接...")
    print("-------------------")

    flag = check_wlan() # checking connection and assign flag

    # Wait for next check
    print("-------------------")
    if flag:
        print("已连接上GitHub，程序自动结束。") 
        break
    else:
        for i in range(wait, 0, -1):
            print("\r还有{}秒进行下一次测试...".format(i), end="")
            time.sleep(1)

    # Cross-platform method to clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
    
# INFO 日志
print("--------[INFO]--------")
print("总共尝试了{}次连接".format(count))
now = datetime.now().strftime("%H:%M:%S") # 获取当前时间并格式化输出
print("连接成功时间：", now)

input("按Enter键继续...")
