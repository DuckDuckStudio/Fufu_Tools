import tkinter as tk
from tkinter import messagebox
import os
import sys
from configparser import ConfigParser
import ctypes
import sys

def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        # 重新启动程序以获取管理员权限，以无控制台窗口方式
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0x40010)
        sys.exit(1)

# 打开程序的函数
def open_program(program_path):
    if program_path == ".\\unins000.exe":
        messagebox.showinfo("提示", "即将启动卸载程序，主程序即将退出。")
        try:
            os.startfile(program_path)
        except AttributeError:
            # os.startfile() 在 Unix 系统上不可用
            os.system(f'start {program_path}')
        except Exception as e:
            messagebox.showerror("错误", f"无法打开: {e}")
        sys.exit()# 结束后退出
    elif program_path == "CheckINFO":
        if messagebox.askyesno("芙芙工具箱", "是否在本地保存相关信息?"):
            program_path = ".\\Check_INFO_save.bat"
        else:
            program_path = ".\\Check_INFO.bat"
    elif program_path == "https://github.com/DuckDuckStudio/Fufu_Tools/issues":
        messagebox.showinfo("提示", "在反馈问题前请先查阅文档中是否已列出解决办法！")
    elif program_path == "https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/online_tools/index.html":
        messagebox.showinfo("提示", "在线工具需要连接网络才能使用，请确认网络已链接！")
        # 继续 ↓
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

# ------- 版本更新检查 ------
try:
    config = ConfigParser(comment_prefixes=[])
    script_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    config_path = os.path.join(script_path, "config.ini")
    config.read(config_path, encoding='utf-8')
    aruic = config.get('settings', 'always_run_update_info_check')
except PermissionError:
    run_as_admin()
# ARUIC表示always_run_update_info_check = 总是运行更新信息检查
if aruic == "True":
    os.startfile(".\\【测试】更新信息提示程序（后台）.exe")
# ------- 可       选 -------
# ------- 启动计数 ----------
start_count = config.getint('count', 'start_count')
start_count += 1
start_count = str(start_count)
config['count']['start_count'] = start_count
try:
    with open(config_path, 'w') as configfile:
        config.write(configfile)
except PermissionError:
    run_as_admin()
# --------------------------

# 创建主窗口
root = tk.Tk()
root.title("芙芙工具箱")

# 设置图标
icon_path = '.\\ico.ico'
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
        "检测网络连接状况": ".\\Tools\\连接检测\\网络连接检测.exe",
        "检测GitHub连接状况": ".\\Tools\\连接检测\\GitHub连接检测.exe",
        "查看网络密码": ".\\Tools\\查看网络密码\\查看网络密码.exe",
    },
    "编解码": {
        "摩斯密码编码": ".\\Tools\\摩斯密码\编码.exe",
        "摩斯密码解码": ".\\Tools\\摩斯密码\\解码.exe",
        "URL编码": ".\\Tools\\URL编解码\\编码.exe",
        "URL解码": ".\\Tools\\URL编解码\\解码.exe",
    },
    "搜索": {
        "批量搜索": ".\\Tools\搜索\\批量搜索.exe",
        "爬取网站搜索结果": ".\\Tools\\搜索\\爬取搜索.exe",
        "打开百度": "https://www.baidu.com/",
    },
    "关于时间": {
        "系统时间显示": ".\\Tools\\系统时间显示\\time.exe",
        "在线自动校准系统时间": ".\\Tools\\校准系统时间\\在线自动校准.exe",
        "手动校准系统时间": ".\\Tools\\校准系统时间\\手动校准系统时间.bat",
    },
    "自动化": {
        "自动左键连点": ".\\Tools\\自动化\\连按\\自动左键连点.exe",
        "自动按键连按": ".\\Tools\\自动化\\连按\\自动按键连按.exe",
        "连续尝试执行命令": ".\\Tools\\自动化\\连续尝试\\连续尝试all.exe",
    },
    "查找": {
        "按文件名查找文件": ".\\Tools\\查找文件\\相同文件名.exe",
        "按文件格式查找文件": ".\\Tools\\查找文件\\相同文件格式.exe",
        "按特定内容查找文件": ".\\Tools\\查找文件\\含有指定内容.exe",
    },
    "关于文件": {
        "强制删除文件夹": ".\\Tools\\删除\\强制删除文件夹.bat",
        "删除指定格式文件": ".\\Tools\\删除\\删除指定格式文件.exe",
        "创建文件": ".\\Tools\\创建文件\\创建文件.exe",
        "文件分类": ".\\Tools\\文件分类\\文件分类.exe",
        "文件下载": ".\\Tools\\文件下载\\文件下载.exe",
        "隐藏文件到图片": ".\\Tools\\隐藏文件\\将文件隐藏在图片中.exe",
    },
    "去除代码注释": {
        "Python注释": ".\\Tools\\去除代码注释\\remove_python_comments.exe",
        "html注释": ".\\Tools\\去除代码注释\\remove_html_comments.exe",
        "C风格注释": ".\\Tools\\去除代码注释\\remove_c_style_comments.exe",
        "批处理(bat)注释": ".\\Tools\\去除代码注释\\remove_batch_comments.exe",
    },
    "其他小工具": {
        "缓存清理": ".\\Tools\\缓存清理\\缓存清理.exe",
        "随机密码生成": ".\\Tools\\随机密码生成\\随机密码生成.exe",
        "随机内容展示": ".\\Tools\\随机展示\\main.exe",
        "查看电脑配置": ".\\Tools\\查看电脑配置\查看电脑配置.exe",
        "进制转换": ".\\Tools\\进制转换\\进制转换.exe",
        "颜色代码展示": ".\\Tools\\颜色代码展示\\ColorDisplay.html",
        "哈希值校验": ".\\Tools\\哈希值校验\\main.exe",
        "获取目录中的文件名": ".\\Tools\\文件名\\获取.exe",
        "[设置自启动]休息一下": ".\\Tools\\休息一下\自启动设置.exe",
        "[主程序]休息一下": ".\\Tools\\休息一下\\休息一下.exe",
        "字母大小写互换": ".\\Tools\\字母大小写互换\\字母大小写互换.exe",
        "英翻中": ".\\Tools\\翻译\\翻译.exe",
    },
    "[实验性工具]": {
        "[实验性小工具说明]": ".\\Text\\【实验性小工具说明】.txt",
        "自动替换指定文本": ".\\Tools\\【实验性工具】\\自动化\\自动替换指定文本\\main.exe",
        "Pyinstaller批量打包": ".\\Tools\\【实验性工具】\\自动化\\自动打包所有py文件\\使用Pyinstaller.exe",
        "Nuitka批量打包": ".\\Tools\\【实验性工具】\\自动化\\自动打包所有py文件\\使用Nuitka.exe",
        "音频base64编解码": ".\\Tools\\【实验性工具】\\音频处理\\音频base64.exe",
        "批量水印添加": ".\\Tools\\【实验性工具】\\图片处理\\批量水印.exe",
        "[Warn]批量水印添加": ".\\Tools\\【实验性工具】\\图片处理\\Warn.txt",
        "视频音频提取": ".\\Tools\\【实验性工具】\\音频处理\\视频中提取.py",
        "定时闹钟": ".\\Tools\\【实验性工具】\\定时闹钟\闹钟.exe",
        "定时闹钟自定义铃声文件夹": ".\\Tools\\【实验性工具】\\定时闹钟\\铃声文件\\",# Wran
        "时间单位转换": ".\\Tools\\【实验性工具】\\知一求多\\单位转换\\时间单位转换.exe",
        "长度单位转换": ".\\Tools\\【实验性工具】\\知一求多\\单位转换\\长度单位转换.exe",
        "圆的参数计算": ".\\Tools\\【实验性工具】\\知一求多\\圆的参数\\圆的参数计算器.exe",
        "搜索引擎索引检测": ".\\Tools\\【实验性工具】\\搜索\\url搜索引擎收录检测.exe",
        "水下音效": ".\\Tools\\【实验性工具】\\水下音效\\main.html",
        "[Warn]水下音效": ".\\Tools\\【实验性工具】\\水下音效\\Warn.txt",
        "去除html注释&删除空行": ".\\Tools\\去除代码注释\\[实验性]remove_html_comments_noenter.exe",
        "在线工具": "https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/online_tools/index.html",
    },
    "关于芙芙工具箱": {
        "检查版本": ".\\Show_version.exe",
        "另存配置文件": ".\\temporarily\\config-save.exe",
        "安装文件夹": os.getcwd(),
        "程序文档": "https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/",
        "程序官网": "https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/",
        "作者网站": "https://duckduckstudio.github.io/yazicbs.github.io/zh_cn/index.html",
        "检查更新": ".\\【测试】更新信息提示程序（后台）.exe",
        "最新开源许可文件": "https://github.com/DuckDuckStudio/Fufu_Tools/blob/main/LICENSE",
        "信息确认": "CheckINFO",
        "问题反馈": "https://github.com/DuckDuckStudio/Fufu_Tools/issues",
        # ONLY FOR EXE SETUP
        "卸载": ".\\unins000.exe",
    },
    # 更多类别和程序...
}

# 初始显示所有类别
show_categories()

# 设置窗口透明度
root.wm_attributes('-alpha', 0.9)

# 运行主循环
root.mainloop()
