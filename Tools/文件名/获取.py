import os
import sys
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore
import configparser

init(autoreset=True) # 初始化 Colorama，使颜色输出生效
output_file = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), '获取结果.txt')
config_file = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'config.ini')

def get_relative_path(file, base_folder):
    # 获取文件相对于基础文件夹的相对路径
    return os.path.relpath(file, base_folder)

def list_files(directory, ignored_formats, specified_formats, ignored_folders):
    # 列出指定目录下的所有文件，并忽略指定格式的文件和文件夹
    file_list = []
    ignored_folders_list = []
    for root, dirs, files in os.walk(directory):
        # 过滤忽略的文件夹
        for ignored_folder in ignored_folders:
            if ignored_folder in dirs:
                ignored_folders_list.append(os.path.join(root, ignored_folder))
                dirs.remove(ignored_folder)
        for file in files:
            _, ext = os.path.splitext(file)
            if specified_formats[0] != "No_Specified":
                # 如果指定了文件格式，则只处理指定格式的文件
                if ext.lower()[1:] in specified_formats:
                    file_path = os.path.join(root, file)
                    file_list.append(file_path)
                else:
                    print(Fore.BLUE + f"[INFO] 文件 {get_relative_path(os.path.join(root, file), directory)} 不在指定的文件格式中，已忽略。")
            elif ignored_formats[0] != "No_Ignored":
                if ext.lower()[1:] not in ignored_formats:
                    # 如果没有指定文件格式，则使用默认规则忽略特定格式的文件
                    file_path = os.path.join(root, file)
                    file_list.append(file_path)
                else:
                    print(Fore.BLUE + f"[INFO] 文件 {get_relative_path(os.path.join(root, file), directory)} 被配置文件忽略。")
            else:# 如果没有特殊、没有忽略
                file_path = os.path.join(root, file)
                file_list.append(file_path)
    for ignored_folder in ignored_folders_list:
        print(Fore.BLUE + f"[INFO] 文件夹 {get_relative_path(ignored_folder, directory)} 被配置文件忽略。")
    return file_list

def write_to_txt(file_list, output_file, base_folder):
    # 将文件列表写入到指定的txt文件中
    with open(output_file, 'w') as f:
        for file in file_list:
            relative_path = get_relative_path(file, base_folder)
            f.write(relative_path + '\n')

def main():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file)
    ignored_formats = config.get('get', 'Ignored file format').split(',')
    specified_formats = config.get('get', 'Specified file format', fallback='').split(',')
    ignored_folders = config.get('get', 'Ignored folders').split(',')

    # 创建GUI窗口，让用户选择文件夹
    root = tk.Tk()
    root.withdraw() # 隐藏主窗口

    folder_path = filedialog.askdirectory(title="请选择文件夹") # 弹出文件夹选择对话框

    if not folder_path:
        print(Fore.RED + "未选择文件夹，请重新运行程序并选择文件夹。")
        return

    # 获取文件夹下的所有文件
    files = list_files(folder_path, ignored_formats, specified_formats, ignored_folders)

    # 将结果写入到txt文件中
    write_to_txt(files, output_file, folder_path)
    print(Fore.GREEN + f"文件列表已保存到{output_file}")

    os.system("start " + output_file)

if __name__ == "__main__":
    main()
