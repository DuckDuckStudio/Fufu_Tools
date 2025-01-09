import os
from colorama import init, Fore

init(autoreset=True)
acount = 0
countd = 0

folder_path = input("请输入文件夹路径:")

if folder_path.startswith(("'", '"')) and folder_path.endswith(("'", '"')):
    folder_path = folder_path[1:-1]

if not folder_path.endswith('\\'):
    folder_path += '\\'

if not os.path.exists(folder_path):
    print(f"{Fore.RED}✕{Fore.RESET} 指定的目录路径不存在，请重新运行程序并输入有效的目录路径。")
    input("按 ENTER 键继续...")
    exit()

print(f"{Fore.GREEN}✓{Fore.RESET} 选取的文件夹路径: {folder_path}")

# --------

file_extension = input("请输入你要查找文件的格式：")

if not file_extension.startswith('.'):
    file_extension = '.' + file_extension

print(f"{Fore.GREEN}✓{Fore.RESET} 要删除的文件格式: {file_extension}")

# -------- 获取参数 ↑ | 操作 ↓ ---------

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(file_extension):
            file_path = os.path.join(root, file)
            acount += 1

print(f"一共找到 {Fore.BLUE} {acount} {Fore.RESET} 个符合条件的文件。")

# 删除指定格式的文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(file_extension):
            file_path = os.path.join(root, file)
            countd += 1
            os.remove(file_path)
            print(f'已删除文件: {file_path} (还剩 {Fore.BLUE} {acount-countd} {Fore.RESET} 个文件)')

print(f"{Fore.GREEN}✓ 文件删除完成！{Fore.RESET}总共删除了 {Fore.BLUE} {countd} {Fore.RESET} 个原文件")

input ("按 Enter 键退出...")