import os
import re
import sys
import base64
import tkinter as tk
from colorama import Fore
from tkinter import filedialog

# ----- init -----
script_folder = os.path.dirname(os.path.abspath(sys.argv[0]))
input_file_path = os.path.join(script_folder, "input.txt")
output_file_path = os.path.join(script_folder, "output.txt")
# ----------------

# ----- 函数 -----
def input_file ():# 解为audio使用
    try:
        with open(input_file_path, "w") as file:
            file.write("请在此处输入所需信息并覆盖掉本条提示，请确保没有其他信息。")
        os.startfile(input_file_path)
        input("请在编辑并保存完你的输入后按Enter键继续...")
        with open(input_file_path, "rb") as file:
            input_data = file.read()
        return input_data
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 文件处理出错:\n{Fore.RED}{e}{Fore.RESET}")
        return "ERROR"

def output_file (base64_data):# 编为base64使用
    try:
        with open(output_file_path, "wb") as output:
            output.write(base64_data)
        print(f"{Fore.GREEN}✓{Fore.RESET} 结果已保存到 {Fore.BLUE}{output_file_path}{Fore.RESET}")
        os.startfile(output_file_path)
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 文件处理出错:\n{Fore.RED}{e}{Fore.RESET}")

def base64_to_audio ():
    base64_data = input_file()
    if base64_data != "ERROR":
        try:
            audio_data = base64.b64decode(base64_data)
            output_folder = filedialog.askdirectory(title="请选择导出文件夹")
            if not output_folder:
                print(f"{Fore.RED}✕{Fore.RESET} 请选择一个文件夹")
                return
            output_name = input("请输入导出的文件的文件名: ")
            output_name = output_name + (".mp3" if not output_name.endswith(".mp3") else "")# 自动补全后缀
            if not output_name:
                print(f"{Fore.RED}✕{Fore.RESET} 文件名不能为空")
                return
            elif re.search(r'[\\/:*?"<>|]', output_name):
                print(f"{Fore.RED}✕{Fore.RESET} 文件名不合法")
                return
            output = os.path.join(output_folder, output_name)
            output = os.path.normpath(output)# 统一斜杠
            with open(output, "wb") as audio_file:
                audio_file.write(audio_data)
            print(f"{Fore.GREEN}✓{Fore.RESET} 已将结果保存至 {Fore.BLUE}{output}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}✕{Fore.RESET} 处理时出错:\n{Fore.RED}{e}{Fore.RESET}")

def audio_to_base64 (audio_file):
    try:
        with open(audio_file, "rb") as audio:
            audio_data = audio.read()
        base64_data = base64.b64encode(audio_data)
        output_file(base64_data)
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 编码时出现错误:\n{Fore.RED}{e}{Fore.RESET}")
# --------------

# ----- main -----
def main ():
    root = tk.Tk()
    root.withdraw()
    print("[音频base64处理程序]")
    print(f"请选择你需要进行的操作:\n{Fore.BLUE}1.{Fore.RESET} 将音频编为base64\n{Fore.BLUE}2.{Fore.RESET} 将base64解为mp3音频")
    user_input = input(f"{Fore.BLUE}?{Fore.RESET} 你的选择是: ").lower()
    if user_input in ["1", "编码", "将音频编为base64", "1.将音频编为base64", "a"]:
        audio_file = filedialog.askopenfilename(title="请选择音频文件")
        if audio_file:
            print(f"{Fore.GREEN}✓{Fore.RESET} 已选取音频文件: {Fore.BLUE}{audio_file}{Fore.RESET}")
            audio_to_base64(audio_file)
        else:
            print(f"{Fore.RED}✕{Fore.RESET} 请选择一个音频文件，重启程序以重试。")
            return
    elif user_input in ["2", "解码", "将base64解为mp3音频", "2.将base64解为mp3音频", "b"]:
        base64_to_audio()
    else:
        print(f"{Fore.RED}✕{Fore.RESET} 请选择一个正确的项")

if __name__ == "__main__":
    main()
    input("按Enter键退出...")
# ----------------


# TEST Note
# 编码 >>> PASS
# 解码 >>> NaN
