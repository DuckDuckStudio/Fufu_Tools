import requests
from plyer import notification
import time
import os

def check_wlan():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get("https://www.github.com/", headers=headers)
        if response.status_code == 200:
            print("连接成功!")
            notification.notify(
                title='GitHub连接状态',
                message='您的计算机可以连接到GitHub啦！',
                timeout=10
            )
        else:
            print("连接失败！状态代码:", response.status_code)
    except Exception as e:
        print("连接失败！")
        print("错误代码:", e)

#---

while True:
    print("正在尝试连接...")
    print("-------------------")

    check_wlan() # checking connection

    # Wait for next check
    print("-------------------")
    for i in range(10, 0, -1):
        print("\r还有{}秒进行下一次测试...".format(i), end="")
        time.sleep(1)

    # Cross-platform method to clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
