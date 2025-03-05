import os
import tkinter as tk
import win32com.client
from tkinter import messagebox
from configparser import ConfigParser

os.chdir(os.path.dirname(os.path.abspath(__file__))) # 避免意外的输出位置

# ------ 检测开始菜单图标情况 ----------
shortcut_path = os.path.join(os.path.join(os.getenv('APPDATA'), "Microsoft\\Windows\\Start Menu\\Programs"), "芙芙工具箱.lnk")
script_path = os.path.realpath(__file__)
icon_path = os.path.join(os.path.dirname(script_path), "ico.ico")

if os.path.exists(shortcut_path):
    link = "从开始菜单中移除"
else:
    link = "添加到开始菜单"
# ---------------------------------

# 创建快捷方式
def create_shortcut(shortcut_path, target_path, icon_path=None):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target_path
    if icon_path:
        shortcut.IconLocation = icon_path
    shortcut.Save()

# 打开程序的函数
def open_program(program_path):
    if program_path == "https://github.com/DuckDuckStudio/Fufu_Tools/issues":
        messagebox.showinfo("提示", "在反馈问题前请先查阅文档中是否已列出解决办法！")
    elif program_path == "link":
        global link # 表明link变量使用的是全局的link而不是函数的link
        if link == "从开始菜单中移除":
            os.remove(shortcut_path)
            link = "添加到开始菜单"
            messagebox.showinfo("提示", "已将芙芙工具箱从开始菜单中移除！")
        elif link == "添加到开始菜单":
            create_shortcut(shortcut_path, script_path, icon_path)
            link = "从开始菜单中移除"
            messagebox.showinfo("提示", "已将芙芙工具箱添加进开始菜单中！")
        return # 不执行接下来的打开代码
    elif program_path == "CheckINFO":
        if messagebox.askyesno("芙芙工具箱", "是否在本地保存相关信息?"):
            program_path = ".\\Check_INFO_save.bat"
        else:
            program_path = ".\\Check_INFO.bat"
    elif program_path == "https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/online_tools/index.html":
        messagebox.showinfo("提示", "在线工具需要连接网络才能使用，请确认网络已链接！")
        # 继续 ↓
    elif program_path == ".\\Tools\\【实验性工具】\\危险区域\\":
        if not messagebox.askyesno("三思而后行", "如果不是文档或维护者提出使用，请不要使用危险区域的脚本。\n一定要使用?"):
            return
    # ---
    try:
        os.startfile(program_path)
    except AttributeError:
        # os.startfile() 在 Unix 系统上不可用
        os.system(f'start {program_path}')
    except Exception as e:
        messagebox.showerror("错误", f"无法打开: {e}")

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

# ------- 版本更新检查 ------
config = ConfigParser(comment_prefixes=[])
config.read("config.ini", encoding='utf-8')
aruic = config.get('settings', 'always_run_update_info_check')
# ARUIC表示always_run_update_info_check = 总是运行更新信息检查
if aruic == "True":
    os.startfile(".\\【测试】更新信息提示程序（后台）.pyw")
# ------- 可       选 -------
# ------- 启动计数 ----------
start_count = config.getint('count', 'start_count')
if start_count == 0:# 首次启动查看LICENSE文件
    os.startfile("https://github.com/DuckDuckStudio/Fufu_Tools/blob/main/LICENSE")
    messagebox.showinfo("提示", "检测到您为首次运行本工具，请先阅读许可文件，使用本工具即表示您同意许可文件中的内容。")
start_count += 1
start_count = str(start_count)
config['count']['start_count'] = start_count
with open("config.ini", 'w') as configfile:
    config.write(configfile)
# --------------------------

# 创建主窗口
root = tk.Tk()
root.title("芙芙工具箱")

# 设置图标
root.iconbitmap(icon_path)

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
    "关于网络": {
        "检测网络连接状况": ".\\Tools\\连接检测\\网络连接检测.py",
        "检测GitHub连接状况": ".\\Tools\\连接检测\\GitHub连接检测.py",
        "查看网络密码": ".\\Tools\\查看网络密码\\查看网络密码.py",
    },
    "编解码": {
        "摩斯密码编码": ".\\Tools\\摩斯密码\\编码.exe",
        "摩斯密码解码": ".\\Tools\\摩斯密码\\解码.exe",
        "URL编码": ".\\Tools\\URL编解码\\编码.py",
        "URL解码": ".\\Tools\\URL编解码\\解码.py",
        "音频base64编解码": ".\\Tools\\音频处理\\音频base64.py",
    },
    "搜索": {
        "批量搜索": ".\\Tools\\搜索\\批量搜索.pyw",
        "爬取网站搜索结果": ".\\Tools\\搜索\\爬取搜索.pyw",
        "打开百度": "https://www.baidu.com/",
    },
    "关于时间": {
        "系统时间显示": ".\\Tools\\系统时间显示\\time.pyw",
        "在线自动校准系统时间": ".\\Tools\\校准系统时间\\在线自动校准.py",
        "手动校准系统时间": ".\\Tools\\校准系统时间\\手动校准系统时间.bat",
    },
    "自动化": {
        "自动左键连点": ".\\Tools\\自动化\\连按\\自动左键连点.py",
        "自动按键连按": ".\\Tools\\自动化\\连按\\自动按键连按.py",
        "连续尝试执行命令": ".\\Tools\\自动化\\连续尝试\\连续尝试all.py",
    },
    "查找": {
        "按文件名查找文件": ".\\Tools\\查找文件\\相同文件名.py",
        "按文件格式查找文件": ".\\Tools\\查找文件\\相同文件格式.py",
        "按特定内容查找文件": ".\\Tools\\查找文件\\含有指定内容.py",
    },
    "关于文件": {
        "强制删除文件夹": ".\\Tools\\删除\\强制删除文件夹.bat",
        "删除指定格式文件": ".\\Tools\\删除\\删除指定格式文件.py",
        "创建文件": ".\\Tools\\创建文件\\创建文件.exe",
        "文件分类": ".\\Tools\\文件分类\\文件分类.py",
        "文件下载": ".\\Tools\\文件下载\\文件下载.py",
        "隐藏文件到图片": ".\\Tools\\隐藏文件\\将文件隐藏在图片中.py",
    },
    "去除代码注释": {
        "Python注释": ".\\Tools\\去除代码注释\\remove_python_comments.py",
        "C风格注释": ".\\Tools\\去除代码注释\\remove_c_style_comments.py",
        "批处理(bat)注释": ".\\Tools\\去除代码注释\\remove_batch_comments.py",
    },
    "知一求多": {
        "时间单位转换": ".\\Tools\\知一求多\\单位转换\\时间单位转换.pyw",
        "长度单位转换": ".\\Tools\\知一求多\\单位转换\\长度单位转换.pyw",
        "圆的参数计算": ".\\Tools\\知一求多\\圆的参数\\圆的参数计算器.pyw",
    },
    "其他小工具": {
        "缓存清理": ".\\Tools\\缓存清理\\缓存清理.py",
        "随机密码生成": ".\\Tools\\随机密码生成\\随机密码生成.py",
        "随机内容展示": ".\\Tools\\随机展示\\main.pyw",
        "视频音频提取": ".\\Tools\\音频处理\\视频中提取.py",
        "查看电脑配置": ".\\Tools\\查看电脑配置\\查看电脑配置.py",
        "进制转换": ".\\Tools\\进制转换\\进制转换.exe",
        "颜色代码展示": ".\\Tools\\颜色代码展示\\ColorDisplay.html",
        "哈希值校验": ".\\Tools\\哈希值校验\\main.py",
        "获取目录中的文件名": ".\\Tools\\文件名\\获取.py",
        "[设置自启动]休息一下": ".\\Tools\\休息一下\\自启动设置.py",
        "[主程序]休息一下": ".\\Tools\\休息一下\\休息一下.pyw",
        "字母大小写互换": ".\\Tools\\字母大小写互换\\字母大小写互换.exe",
        "英翻中": ".\\Tools\\翻译\\翻译.pyw",
    },
    "[实验性工具]": {
        "[实验性小工具说明]": ".\\Text\\【实验性小工具说明】.txt",
        "自动替换指定文本": ".\\Tools\\【实验性工具】\\自动化\\自动替换指定文本\\main.py",
        "Pyinstaller批量打包": ".\\Tools\\【实验性工具】\\自动化\\自动打包所有py文件\\使用Pyinstaller.py",
        "Nuitka批量打包": ".\\Tools\\【实验性工具】\\自动化\\自动打包所有py文件\\使用Nuitka.py",
        "hosts修改": ".\\Tools\\【实验性工具】\\hosts修改\\调用.py",
        "批量水印添加": ".\\Tools\\【实验性工具】\\图片处理\\批量水印.py",
        "[Warn]批量水印添加": ".\\Tools\\【实验性工具】\\图片处理\\Warn.txt",
        "定时闹钟": ".\\Tools\\【实验性工具】\\定时闹钟\\闹钟.py",
        "定时闹钟自定义铃声文件夹": ".\\Tools\\【实验性工具】\\定时闹钟\\铃声文件\\",# Warn
        "搜索引擎索引检测": ".\\Tools\\【实验性工具】\\搜索\\url搜索引擎收录检测.py",
        "在线工具": "https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/online_tools/index.html",
        "危险区域": ".\\Tools\\【实验性工具】\\危险区域\\",
    },
    "关于芙芙工具箱": {
        "检查版本": ".\\Show_version.py",
        "修改开始菜单图标": "link",
        "另存配置文件": ".\\temporarily\\config-save.py",
        "安装文件夹": os.path.dirname(os.path.abspath(__file__)),
        "程序文档": "https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/",
        "程序官网": "https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/",
        "作者网站": "https://duckduckstudio.github.io/yazicbs.github.io/zh_cn/index.html",
        "检查更新": ".\\【测试】更新信息提示程序（后台）.pyw",
        "最新开源许可文件": "https://github.com/DuckDuckStudio/Fufu_Tools/blob/main/LICENSE",
        "信息确认": "CheckINFO",
        "问题反馈": "https://github.com/DuckDuckStudio/Fufu_Tools/issues",
    },
    # 更多类别和程序...
}

# 初始显示所有类别
show_categories()

# 设置窗口透明度
root.wm_attributes('-alpha', 0.9)

# 运行主循环
root.mainloop()
