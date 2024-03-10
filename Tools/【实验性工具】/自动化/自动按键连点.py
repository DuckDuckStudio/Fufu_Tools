import pyautogui
import keyboard
import time

print("本程序用于自动连按键盘上的按键，左键连点出门左转。")

# 从用户那里获取连续按键间隔时间，并转换为浮点数
click_interval = float(input("请输入每次按键的间隔时间(秒)："))  # 转换为浮点数
key = input("请输入需要连按的按键：")
key = key.lower()

# 控制自动按键的开关
auto_pressing = False

def toggle_auto_press():
    global auto_pressing
    # 切换自动按键状态
    auto_pressing = not auto_pressing
    if auto_pressing:
        print("自动按键 已开始。")
    else:
        print("自动按键 已停止。")

def auto_press():
    while True:
        if auto_pressing:
            pyautogui.press(key)
            time.sleep(click_interval)
        # 这里稍微延迟一下，减少CPU使用率
        time.sleep(0.01)

# 绑定F8键，用于切换自动按键状态
keyboard.add_hotkey('F8', toggle_auto_press)

print("程序已启动，按下F8键开始/停止自动连续按",key,"键。")
auto_press()
