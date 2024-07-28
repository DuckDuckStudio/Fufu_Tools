import datetime
import tkinter as tk

# ----- 以下问题的Issue一律按未计划关闭 -----
# - 一直横向拉长导致日期显示不完整 > 无法实施
# - 窗口过小导致文本无法正常显示 > 无法实施
# - 窗口乱拉大小导致的某些文本错误 > 部分以无法实施/无法重现关闭
# ----- 以下问题的Issue一律按已完成关闭 -----
# - 添加控制是否显示日期

def update_clock():
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

    clock_label.after(1000, update_clock)

def update_text_size():
    # 获取当前窗口的宽度和高度
    width = root.winfo_width()
    height = root.winfo_height()

    # 根据窗口宽度计算新的字体大小
    new_clock_font_size = max(10, int(width / 10))
    new_date_font_size = max(8, int(width / 40))

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
button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10) # 放置按钮的Frame

sticky_button = tk.Button(button_frame, text='置顶', command=toggle_sticky)
sticky_button.pack(side=tk.LEFT) # 将"置顶"按钮放置在左侧

exit_button = tk.Button(button_frame, text='退出', command=on_exit)
exit_button.pack(side=tk.RIGHT) # 将"退出"按钮放置在右侧

# 初始化时更新文本大小
update_text_size()

# 监听窗口尺寸变化事件，动态调整文本大小
root.bind("<Configure>", lambda e: update_text_size())

update_clock()

root.mainloop()
