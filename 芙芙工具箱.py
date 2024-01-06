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
root.title("芙芙工具箱")

# 创建顶部蓝色框
header = tk.Frame(root, bg='#91cbea', pady=10)
header.pack(fill='x')
header_label = tk.Label(header, text="芙芙工具箱", fg='#ffffff', bg='#91cbea', font=("Arial", 24))
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
    "连接检测": {
        "检测网络连接状况": ".\连接检测\网络连接检测.py",
        "检测GitHub连接状况": ".\连接检测\\GitHub连接检测.py",
    },
    "摩斯密码": {
        "摩斯密码编码": ".\摩斯密码\编码.exe",
        "摩斯密码解码": ".\摩斯密码\解码.exe",
    },
    "URL编解码": {
        "URL编码": ".\\URL编解码\编码.py",
        "URL解码": ".\\URL编解码\解码.py",
    },
    "搜索": {
        "批量搜索": ".\搜索\批量搜索\批量搜索.py",
        "爬取网站搜索结果": ".\搜索\爬取搜索\图形化操作界面.py",
    },
    "系统时间校准": {
        "手动校准系统时间": ".\校准系统时间\手动校准系统时间.bat",
        "在线自动校准系统时间": ".\校准系统时间\在线自动校准.exe",
    },
    "其他": {
        "强制删除文件夹": ".\强制删除文件夹\强制删除文件夹.bat",
        "随机密码生成": ".\随机密码生成\随机密码生成.exe",
        "文件分类": ".\文件分类\文件分类.py",
        "文件下载": ".\文件下载\点我下载文件.bat",
        "系统时间显示": ".\系统时间显示\\time.exe",
        "查看电脑配置": ".\查看电脑配置\查看电脑配置.bat",
        "查看网络密码": ".\查看网络密码\查看网络密码.bat",
        "创建文件": ".\创建文件\创建文件.exe",
        "缓存清理": ".\缓存清理\缓存清理.bat",
        "进制转换": ".\进制转换\进制转换.exe",
        "字母大小写互换": ".\字母大小写互换\字母大小写互换.exe",
        "英翻中": ".\翻译\翻译.py",
        "隐藏文件到图片": ".\隐藏文件\将文件隐藏在图片中.py",
    },
    "说明文件": {
        "“进制转换”使用说明": ".\进制转换\使用说明.txt",
        "“摩斯密码编解码”使用说明": ".\摩斯密码\说明.md",
    },
    "关于芙芙工具箱": {
        "检查小工具版本": ".\\Show_version.bat",
        "访问小工具wiki": "https://github.com/DuckDuckStudio/Fufu_Tools.wiki.git",
        "访问作者网站": "https://duckduckstudio.github.io/yazicbs.github.io/zh_cn/index.html",
        "查看开源许可文件": ".\\LICENSE",
        "信息确认": ".\\Check_INFO.bat",
        "信息确认(导出)": ".\\Check_INFO_save.bat",
    },
    # 更多类别和程序...
}

print("这也是我的主程序，请不要把我关掉，不然我会伤心的！")
print()

heart = [
    "  ***       ***  ",
    " *****     ***** ",
    "*******   *******",
    " *************** ",
    "  *************  ",
    "   ***********   ",
    "    *********    ",
    "     *******     ",
    "      *****      ",
    "       ***       ",
    "        *        "
]

for line in heart:
    print(line)


# 初始显示所有类别
show_categories()

# 设置窗口透明度
root.wm_attributes('-alpha', 0.9)

# 运行主循环
root.mainloop()