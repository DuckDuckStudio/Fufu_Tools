import requests
import time
import os
from plyer import notification
import configparser

# READ config.ini file
script_dir = os.path.dirname(os.path.realpath(__file__))
config_file_path = os.path.join(script_dir, "config.ini")
config = configparser.ConfigParser()
config.read(config_file_path)
wait = config.getint('time', 'wait')
url = config.get('url', 'url')
translation = config.getboolean('Translation', 'Error message')

def check_wlan():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    
    if translation:
        try:
            if response.status_code == 200:
                print("连接成功!")
            else:
                print("连接失败！状态代码:", response.status_code)
                notification.notify(
                    title='芙芙工具箱 | 网络连接检测',
                    message=f'检测到异常情况，请注意！({response.status_code})',
                    timeout=10
                )
        except requests.exceptions.Timeout:
            print("连接超时！")
            notification.notify(
                title='芙芙工具箱 | 网络连接检测',
                message='检测到异常情况，请注意！(连接超时)',
                timeout=10
            )
        except requests.exceptions.ConnectionError:
            print("无法连接到远程服务器！")
            notification.notify(
                title='芙芙工具箱 | 网络连接检测',
                message='检测到异常情况，请注意！(无法连接到远程服务器)',
                timeout=10
            )
        except Exception as e:
            print("连接失败！")
            print("错误代码:", e)
            notification.notify(
                title='芙芙工具箱 | 网络连接检测',
                message='检测到异常情况，请注意！',
                timeout=10
            )
    else:
        try:
            if response.status_code == 200:
                print("连接成功!")
            else:
                print("连接失败！状态代码:", response.status_code)
                notification.notify(
                    title='芙芙工具箱 | 网络连接检测',
                    message=f'检测到异常情况，请注意！({response.status_code})',
                    timeout=10
                )
        except Exception as e:
            print("连接失败！")
            print("错误代码:", e)
            notification.notify(
                title='芙芙工具箱 | 网络连接检测',
                message='检测到异常情况，请注意！',
                timeout=10
            )

#---

while True:
    print("正在尝试连接...")
    print("-------------------")

    check_wlan() # checking connection

    # Wait for next check
    print("-------------------")
    for i in range(wait, 0, -1):
        print("\r还有{}秒进行下一次测试...".format(i), end="")
        time.sleep(1)

    # Cross-platform method to clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
