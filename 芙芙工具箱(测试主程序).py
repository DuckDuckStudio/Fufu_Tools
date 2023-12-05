import tkinter as tk
from tkinter import messagebox
import os
import sys

# 打开程序的函数
def open_program(program_path):
    try:
        os.startfile(program_path)
    except AttributeError:
        # os.startfile() 在 Unix 系统上不可用
        os.system(f'start {program_path}')
    except Exception as e:
        messagebox.showerror("错误", f"无法打开程序: {e}")

# 创建类别内容的函数
def show_category(container, programs):
    # 清空容器内的内容
    for widget in container.winfo_children():
        widget.destroy()
    
    # 设置每行最多显示的按钮数量
    max_buttons_per_row = 3
    row, col = 0, 0

    # 在容器中为每个程序添加按钮
    for program_name, program_path in programs.items():
        button = tk.Button(container, text=program_name, command=lambda p=program_path: open_program(p), width=20)
        button.grid(row=row, column=col, padx=10, pady=5)
        col += 1
        
        # 每行显示的按钮数量达到最大值时，换行继续显示
        if col == max_buttons_per_row:
            row += 1
            col = 0

    # 显示返回按钮
    back_button.pack(side='left', padx=10, pady=5)

# 返回类别选择界面
def show_categories():

    # 设置每行最多显示的按钮数量
    max_buttons_per_row = 3
    row, col = 0, 0

    # 清空内容容器
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # 重新添加类别按钮
    row, col = 0, 0
    for category_name, programs in categories.items():
        button = tk.Button(content_frame, text=category_name, command=lambda p=programs: show_category(content_frame, p), width=20)
        button.grid(row=row, column=col, padx=10, pady=5)
        col += 1

        # 每行显示的按钮数量达到最大值时，换行继续显示
        if col == max_buttons_per_row: # 在这里修改最大值
            row += 1
            col = 0
    
    # 隐藏返回按钮
    back_button.pack_forget()

# 创建主窗口
root = tk.Tk()
root.title("工具箱")

# 创建顶部蓝色框
header = tk.Frame(root, bg='#b3dcff', pady=10)
header.pack(fill='x')
header_label = tk.Label(header, text="芙芙工具箱", fg='white', bg='#b3dcff', font=("Arial", 24))
header_label.pack(side='left', padx=20)

# 创建内容容器
content_frame = tk.Frame(root, pady=20)
content_frame.pack(fill='both', expand=True)

# 创建返回按钮，初始时不显示
back_button = tk.Button(root, text="返回", command=show_categories)

# 类别数据，包含类别名称和程序列表
categories = {
    "查找文件": {
        "按文件名查找": ".\查找文件\查找文件（相同文件名）.bat",
        "按文件格式查找": ".\查找文件\查找文件（相同文件名）.bat",
    },
    "创建文件": ".\创建文件\创建文件.exe",
    "缓存清理": ".\缓存清理\缓存清理.bat",
    "进制转换": ".\进制转换\进制转换.exe",
    "连接检测": {
        "检测网络连接状况": ".\连接检测\网络连接检测.py",
        "检测GitHub连接状况": ".\连接检测\\github_notification.py",
    },
    "摩斯密码": {
        "摩斯密码编码": ".\摩斯密码\编码.exe",
        "摩斯密码解码": ".\摩斯密码\解码.exe",
    },
    "其他": {
        "爬取网站搜索结果": ".\爬取网站搜索结果\爬取百度搜索结果.py",
        "强制删除文件夹": ".\强制删除文件夹\强制删除文件夹.bat",
        "随机密码生成": ".\随机密码生成\随机密码生成.exe",
        "文件分类": ".\文件分类\文件分类.py",
        "文件下载": ".\文件下载\点我下载文件.bat",
        "系统时间显示": ".\系统时间显示\\time.exe",
        "校准系统时间": ".\校准系统时间\手动校准系统时间.bat",
        "查看电脑配置": ".\查看电脑配置\查看电脑配置.bat",
        "查看网络密码": ".\查看网络密码\查看网络密码.bat",
        "检查小工具版本": ".\\Show_wersion.bat",
    },
    # 更多类别和程序...
}

# 初始显示所有类别
show_categories()

# 设置窗口透明度
root.wm_attributes('-alpha', 0.9)

# 运行主循环
root.mainloop()