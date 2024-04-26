import pyautogui
import keyboard
import time

# 有效的按键
# 依据文档：https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
valid_keys = [
    '\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
    'browserback', 'browserfavorites', 'browserforward', 'browserhome',
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f9',# 手动去除 f8 键
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
    'command', 'option', 'optionleft', 'optionright'
]

print("本程序用于自动连按键盘上的按键，左键连点出门左转。")

while True:
    try:
        click_interval = float(input("请输入每次按键的间隔时间(秒)："))
        break
    except ValueError:
        print("输入的数据不合法，请重新输入。")

# 获取需要连按的按键
while True:
    key = input("请输入需要连按的按键：")
    key = key.lower()
    if key in valid_keys:
        break
    elif key == "f8":
        print("[WARN]需要自动连按的按键与开启自动连按的按键相同，无法使用！")
        print("请重新输入一个其他按键！")
    else:
        print("输入的按键无效！请重新输入！")

# 控制自动按键的开关
auto_pressing = False

# 控制提示消息
first_time = True

def toggle_auto_press():
    global auto_pressing
    global first_time
    # 切换自动按键状态
    auto_pressing = not auto_pressing
    if first_time:
        print("自动按键 已开始。")# 首次按下F8必定是开始自动按键
        first_time = False # 标记为非首次
    else:
        if auto_pressing:
            print('\033[1A\033[K' + "自动按键 已开始。")
        else:
            print('\033[1A\033[K' + "自动按键 已停止。")

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
