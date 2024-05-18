import os
import shutil
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore

init(autoreset=True)  # 初始化 Colorama，使颜色输出生效

def select_destination_folder():
    print("请选择保存到的文件夹:", end=" ")

    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    destination_folder = filedialog.askdirectory()

    print(f"{Fore.GREEN}\r✔{Fore.RESET} 已选择保存到的文件夹: {Fore.BLUE}{destination_folder}", end=" ")
    return destination_folder

def check_folder(destination_folder):
    # 检测是否选择了文件夹
    if destination_folder == "":
        print(f"\r{Fore.RED}×{Fore.RESET} 未选择文件夹，请先选择一个输出位置。")
        return False
    # 检查目标文件夹是否存在，如果不存在则创建
    if not os.path.exists(destination_folder):
        print(f"\n{Fore.YELLOW}⚠ 目标文件夹不存在，将新建一个同名文件夹。", end=" ")
        os.makedirs(destination_folder)
    # 检查目标文件夹是否为空
    if len(os.listdir(destination_folder)) != 0:
        print(f"\r{Fore.RED}× 错误的目标文件夹: {Fore.BLUE}{destination_folder}\n{Fore.YELLOW}  原因：目标文件夹不为空。")
        return False
    
    print(f"{Fore.GREEN}\r✔{Fore.RESET} 已选择保存到的文件夹: {Fore.BLUE}{destination_folder}")# 刷新，避免被顶掉
    return True # 一切正常

def copy_config_files(destination_folder):
    # 获取当前运行脚本的文件夹路径的上级目录作为源文件夹
    current_folder = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.dirname(current_folder)

    copied_files = []  # 用于存储已经复制的文件路径

    try:
        # 遍历源文件夹中的所有文件和子文件夹
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file == 'config.ini':
                    source_path = os.path.join(root, file)
                    relative_path = os.path.relpath(source_path, source_folder)
                    if root == source_folder:
                        print(f"{Fore.BLUE}[!]{Fore.RESET} 忽略版本配置文件。")
                        continue  # 忽略源文件夹中的config.ini
                    destination_path = os.path.join(destination_folder, relative_path)
                    destination_dir = os.path.dirname(destination_path)
                    
                    # 创建目标文件夹中的子文件夹（如果需要）
                    if not os.path.exists(destination_dir):
                        os.makedirs(destination_dir)
                    
                    # 复制文件
                    shutil.copyfile(source_path, destination_path)
                    copied_files.append(destination_path)  # 记录已复制的文件
                    print(f"已复制配置文件 {Fore.BLUE} {source_path} {Fore.RESET} 到 {Fore.BLUE} {destination_path} {Fore.RESET}。")

        # 如果成功完成所有文件复制，则打印成功消息
        print(f"{Fore.GREEN}✔{Fore.RESET} 已保存配置文件到 {Fore.BLUE} {destination_folder} {Fore.RESET} 中，下次更新可以直接替换配置文件！")

    except KeyboardInterrupt:
        # 用户按下 Ctrl+C 取消操作
        print(f"{Fore.RED}×{Fore.RESET} 用户取消操作.")
        
        for file_path in copied_files:
            os.remove(file_path)  # 删除已复制的文件
        
        print(f"{Fore.RED}×{Fore.RESET} 操作已取消。")

    except Exception as e:
        # 出现异常时取消操作并清空已复制的文件
        print(f"\n{Fore.RED}×{Fore.RESET} 复制文件时发生错误: {str(e)}")
        
        for file_path in copied_files:
            os.remove(file_path)  # 删除已复制的文件
        
        print(f"{Fore.RED}×{Fore.RESET} 出现错误，操作取消.")


# 让用户选择目标文件夹
destination_folder = select_destination_folder()

if check_folder(destination_folder):
    # 调用函数复制config.ini文件
    copy_config_files(destination_folder)
else:
    print(f"{Fore.RED}\r×{Fore.RESET} 出现错误，操作取消.")

input("按Enter键继续")
