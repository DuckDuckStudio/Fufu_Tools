import requests
from plyer import notification
import time

def check_github():
    while True:
        print('正在尝试连接...')
        try:
            response = requests.get('https://github.com')
            if response.status_code == 200:
                print('连接成功！')
                notification.notify(
                    title='GitHub连接状态',
                    message='您的计算机可以连接到GitHub啦！',
                    timeout=10
                )
                break
            else:
                print('连接失败！')
                print()
        except:
            print('连接失败！')
            print()

        time.sleep(10)  # 每10秒检查一次连接状态（时间太小会对网络产生不必要负担）

check_github()
