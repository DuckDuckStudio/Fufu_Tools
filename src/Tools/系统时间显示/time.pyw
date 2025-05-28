import datetime
import tkinter as tk

# ----- 以下问题的Issue一律按未计划关闭 -----
# - 一直横向拉长导致日期显示不完整 > 无法实施
# - 窗口过小导致文本无法正常显示 > 无法实施
# - 窗口乱拉大小导致的某些文本错误 > 部分以无法实施/无法重现关闭
# ----- 以下问题的Issue一律按已完成关闭 -----
# - 添加控制是否显示日期

update_in_progress = False

def update_clock():
    global update_in_progress
    if update_in_progress:
        return
    update_in_progress = True

    now = datetime.datetime.now()

    # 将英文的星期转换为中文
    weekday_mapping = {
        'Monday': '星期一',
        'Tuesday': '星期二',
        'Wednesday': '星期三',
        'Thursday': '星期四',
        'Friday': '星期五',
        'Saturday': '星期六',
        'Sunday': '星期日'
    }
    weekday_str = weekday_mapping[now.strftime('%A')]

    date_str = now.strftime('%Y / %m / %d') + ' ' + weekday_str
    time_str = now.strftime('%H:%M:%S')

    # 更新文本内容
    clock_label.config(text=time_str)
    date_label.config(text=date_str)

    # 更新文本字体大小
    update_text_size()

    update_in_progress = False
    clock_label.after(1000, update_clock)

def update_text_size():
    # 获取当前窗口的宽度和高度
    width = root.winfo_width()

    # 根据窗口宽度计算新的字体大小
    new_clock_font_size = max(10, int(width / 10))
    new_date_font_size = max(8, int(width / 27))

    # 设置新的字体大小
    clock_label.config(font=("Arial", new_clock_font_size))
    date_label.config(font=("Arial", new_date_font_size))

def on_exit():
    root.destroy()

def toggle_sticky():
    if root.attributes('-topmost'):
        root.attributes('-topmost', False)
        sticky_button.config(text='置顶')
    else:
        root.attributes('-topmost', True)
        sticky_button.config(text='取消置顶')

# 工具按钮点击后显示/隐藏工具区
def toggle_tools():
    if tools_frame.winfo_ismapped():
        tools_frame.pack_forget()
        # 解绑点击事件
        root.unbind("<Button-1>")
    else:
        tools_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=6, pady=10)
        # 绑定点击事件
        root.bind("<Button-1>", on_click_outside_tools, add='+')

def on_click_outside_tools(event):
    # 如果点击的是“工具”按钮本身，则不关闭
    if event.widget == tools_button:
        return
    # 判断点击是否在tools_frame内
    # 获取tools_frame的绝对坐标和大小
    x1 = tools_frame.winfo_rootx()
    y1 = tools_frame.winfo_rooty()
    x2 = x1 + tools_frame.winfo_width()
    y2 = y1 + tools_frame.winfo_height()
    # 获取鼠标点击的绝对坐标
    abs_x = event.x_root
    abs_y = event.y_root
    # 如果点击不在tools_frame内，则关闭
    if not (x1 <= abs_x <= x2 and y1 <= abs_y <= y2):
        tools_frame.pack_forget()
        root.unbind("<Button-1>")

# 主题相关配置
themes = {
    "light": {
        "bg": "white",
        "fg": "black",
        "button_bg": "#f0f0f0",
        "button_fg": "black"
    },
    "dark": {
        "bg": "#23272e",
        "fg": "#e6e6e6",
        "button_bg": "#444950",
        "button_fg": "#e6e6e6"
    }
}
current_theme = "light"

def apply_theme(theme_name):
    theme = themes[theme_name]
    root.config(bg=theme["bg"])
    main_frame.config(bg=theme["bg"])
    clock_label.config(bg=theme["bg"], fg=theme["fg"])
    date_label.config(bg=theme["bg"], fg=theme["fg"])
    button_frame.config(bg=theme["bg"])
    tools_button.config(bg=theme["button_bg"], fg=theme["button_fg"])
    tools_frame.config(bg=theme["bg"])
    sticky_button.config(bg=theme["button_bg"], fg=theme["button_fg"])
    exit_button.config(bg=theme["button_bg"], fg=theme["button_fg"])
    theme_button.config(bg=theme["button_bg"], fg=theme["button_fg"])

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme(current_theme)
    theme_button.config(text="浅色主题" if current_theme == "dark" else "深色主题")

root = tk.Tk()
root.title('时钟')

# 设置窗口的大小
win_width = 300
win_height = 180

# 获取屏幕宽高
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 计算窗口的位置
x = (screen_width - win_width) // 2
y = (screen_height - win_height) // 2

root.geometry(f'{win_width}x{win_height}+{x}+{y}') # 设置窗口在屏幕中央

main_frame = tk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor='center') # 将main_frame放置在窗口中央

clock_label = tk.Label(main_frame, font=('Arial', 40))
clock_label.pack()

date_label = tk.Label(main_frame, font=('Arial', 12), pady=10) # 增加垂直间距
date_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

tools_button = tk.Button(button_frame, text='工具', command=toggle_tools)
tools_button.pack(side=tk.LEFT)  # “工具”按钮放左侧

# 工具区，初始隐藏
tools_frame = tk.Frame(root)

sticky_button = tk.Button(tools_frame, text='置顶', command=toggle_sticky)
sticky_button.pack(side=tk.LEFT, padx=5)

# 新增：主题切换按钮
theme_button = tk.Button(tools_frame, text='深色主题', command=toggle_theme)
theme_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(tools_frame, text='退出', command=on_exit)
exit_button.pack(side=tk.LEFT, padx=5)

# 初始化时更新文本大小和主题
update_text_size()
apply_theme(current_theme)

# 监听窗口尺寸变化事件，动态调整文本大小
root.bind("<Configure>", lambda e: update_text_size())

update_clock()

root.mainloop()
