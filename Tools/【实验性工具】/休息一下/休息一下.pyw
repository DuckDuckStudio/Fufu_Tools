# 计时程序开启时间显示提示
# 默认随主程序开启 -> 自启动？
# 隐藏控制台 (pyw)

# 导入
from plyer import notification
import time

# 2h
total_seconds = 2*60*60 # 2h -> 120min -> 7200s
while total_seconds >= 0:
    time.sleep(1)
    total_seconds -= 1

# at 2h
notification.notify(
    title='休息一下吧！',
    message='已经使用设备超过 2 小时了，休息一下吧！\n',
    timeout=10
)

# No more down ...
