import os
import sys
import shutil
import configparser
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def 选择备份文件夹():
    root = tk.Tk()
    root.withdraw()
    备份文件夹 = filedialog.askdirectory(title="你之前将配置文件备份到了哪里？")
    if not 备份文件夹:
        messagebox.showerror("错误", "未选择文件夹，操作取消。")
        sys.exit(3)
    elif not os.path.exists(备份文件夹):
        messagebox.showerror("错误", "备份文件夹不存在")
    return 备份文件夹

def 比较配置文件键(文件1: str, 文件2: str):
    config1 = configparser.ConfigParser()
    config2 = configparser.ConfigParser()
    
    try:
        config1.read(文件1)
        config2.read(文件2)
    except Exception as e:
        return False, f"配置文件解析失败: {str(e)}"

    # 比较所有节
    sections1 = set(config1.sections())
    sections2 = set(config2.sections())
    if sections1 != sections2:
        return False, f"节不一致: 备份文件节={sections1}，目标文件节={sections2}"

    # 比较每个节内的键
    for section in sections1:
        keys1 = set(config1[section].keys())
        keys2 = set(config2[section].keys())
        if keys1 != keys2:
            return False, f"节 [{section}] 中: 备份文件键={keys1}，目标文件键={keys2}"

    return True, "键完全一致"

def 还原配置文件(备份文件夹: str, 目标根目录: str):
    已处理文件 = 0
    跳过文件 = 0

    for root, _, files in os.walk(备份文件夹):
        for file in files:
            if file == 'config.ini':
                备份路径 = os.path.join(root, file)
                相对路径 = os.path.relpath(备份路径, 备份文件夹)
                目标路径 = os.path.join(目标根目录, 相对路径)

                # 检查目标文件是否存在
                if not os.path.exists(目标路径):
                    messagebox.showwarning("警告", f"您使用的版本中不存在配置文件 {相对路径}，跳过还原。")
                    跳过文件 += 1
                    continue

                # 比较键
                键一致, 信息 = 比较配置文件键(备份路径, 目标路径)
                if not 键一致:
                    messagebox.showwarning("警告", f"您使用的版本中的配置文件 {相对路径} 与您备份的配置文件的键不一致，跳过还原。\n{信息}")
                    跳过文件 += 1
                    continue

                # 覆盖文件
                try:
                    shutil.copyfile(备份路径, 目标路径)
                    已处理文件 += 1
                except Exception as e:
                    messagebox.showerror("错误", f"还原配置文件 {相对路径} 失败:\n{str(e)}")
                    跳过文件 += 1

    messagebox.showinfo("恭喜", f"成功还原配置文件！\n一共成功还原了 {已处理文件} 个配置文件，跳过了 {跳过文件} 个配置文件。")

def main():
    备份文件夹 = 选择备份文件夹()
    
    脚本路径 = os.path.abspath(sys.argv[0])
    目标根目录 = os.path.dirname(os.path.dirname(脚本路径))

    还原配置文件(备份文件夹, 目标根目录)

if __name__ == "__main__":
    main()
