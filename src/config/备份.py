import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from colorama import init, Fore

def 选择目标文件夹():
    while True:
        root = tk.Tk()
        root.withdraw() # 隐藏主窗口

        目标文件夹 = filedialog.askdirectory(title="你要将配置文件备份到哪里？")

        if 检查文件夹(目标文件夹):
            return 目标文件夹

def 检查文件夹(目标文件夹):
    # 检测是否选择了文件夹
    if not 目标文件夹:
        # 当用户点击选择文件窗口的“取消”按钮时
        messagebox.showerror("错误", "未选择文件夹，操作取消。")
        sys.exit(3)
        # return False
    # 检查目标文件夹是否存在，如果不存在则创建
    if not os.path.exists(目标文件夹):
        messagebox.showwarning("警告", "目标文件夹不存在，将新建一个同名文件夹。")
        os.makedirs(目标文件夹)
    # 检查目标文件夹是否为空
    if len(os.listdir(目标文件夹)) != 0:
        messagebox.showerror("错误", "目标文件夹不为空，请选择一个空文件夹。")
        return False
    return True # 一切正常

def 复制配置文件(目标文件夹):
    # 获取当前运行脚本的文件夹路径的上级目录作为源文件夹
    当前文件夹 = os.path.dirname(os.path.abspath(sys.argv[0]))
    源文件夹 = os.path.dirname(当前文件夹)

    已复制的文件 = []  # 用于存储已经复制的文件路径

    try:
        # 遍历源文件夹中的所有文件和子文件夹
        for root, dirs, files in os.walk(源文件夹):
            for file in files:
                if file == 'config.ini':
                    源路径 = os.path.join(root, file)
                    if root == 源文件夹:
                        # 忽略源文件夹中的 config.ini
                        continue
                    目标路径 = os.path.join(目标文件夹, os.path.relpath(源路径, 源文件夹))
                    目标目录 = os.path.dirname(目标路径)

                    # 创建目标文件夹中的子文件夹（如果需要）
                    if not os.path.exists(目标目录):
                        os.makedirs(目标目录)
                    
                    # 复制文件
                    shutil.copyfile(源路径, 目标路径)
                    已复制的文件.append(目标路径)  # 记录已复制的文件

        # 如果成功完成所有文件复制
        messagebox.showinfo("恭喜", "配置文件备份成功！")
    except KeyboardInterrupt:
        # 用户按下 Ctrl+C 取消操作
        messagebox.showerror("错误", "用户已取消操作。")
        
        for file_path in 已复制的文件:
            os.remove(file_path) # 删除已复制的文件
    except Exception as e:
        # 出现异常时取消操作并清空已复制的文件
        messagebox.showerror("错误", f"备份过程中出现错误:\n{e}")

        for file_path in 已复制的文件:
            os.remove(file_path)  # 删除已复制的文件


def main():
    init(autoreset=True)
    # 让用户选择目标文件夹
    目标文件夹 = 选择目标文件夹()
    复制配置文件(目标文件夹)

if __name__ == "__main__":
    main()
