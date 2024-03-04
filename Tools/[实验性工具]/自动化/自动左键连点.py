import pyautogui
import keyboard
import time

# 从用户那里获取连续点击间隔时间，并转换为浮点数
click_interval = float(input("请输入每次点击的间隔时间(秒)："))  # 转换为浮点数

# 控制自动点击的开关
auto_clicking = False

def toggle_auto_click():
    global auto_clicking
    # 切换自动点击状态
    auto_clicking = not auto_clicking
    if auto_clicking:
        print("自动点击 已开始。")
    else:
        print("自动点击 已停止。")

def auto_click():
    while True:
        if auto_clicking:
            pyautogui.click()
            time.sleep(click_interval)
        # 这里稍微延迟一下，减少CPU使用率
        time.sleep(0.01)

# 绑定F8键，用于切换自动点击状态
keyboard.add_hotkey('F8', toggle_auto_click)

print("程序已启动，按下F8键开始/停止自动左键连续点击。")
print("直接关闭窗口可退出本程序。")
auto_click()
