import os
import sys
import configparser
import subprocess
from colorama import init, Fore

# ------ 初始化 --------
init(autoreset=True)
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
config = configparser.ConfigParser()
config.read('config.ini')
check_directory = input("请输入目录：")
# 验证
if check_directory.startswith(("'", '"')) and check_directory.endswith(("'", '"')):
    check_directory = check_directory[1:-1]

if not check_directory.endswith('\\'):
    check_directory += '\\'

if not os.path.exists(check_directory):
    print("指定的目录路径不存在，请重新运行程序并输入有效的目录路径。")
    input("按 ENTER 键继续...")
    exit()
# ----------------------

# --------- 构建调用命令函数 -----------
def build_Check_the_trailing_space_call_command(directory):
    """
    usage: 尾随空格.py [-h] [--file_extensions FILE_EXTENSIONS] --dir DIRECTORY

    检查指定目录下的文件是否存在尾随空格

    options:
    -h, --help                                 show this help message and exit
    --file_extensions FILE_EXTENSIONS          要检查的文件扩展名列表，以 , 分隔
    --dir DIRECTORY                            要检查的目录路径
    """
    file_extensions = config.get('Check_trailing_space', 'FileExtensions')
    
    if isinstance(file_extensions, list):
        file_extensions = ','.join(file_extensions)

    command = f'python 代码校对\\尾随空格.py --dir {directory}'
    if file_extensions:
        command += f' --file_extensions {file_extensions}'

    subprocess.run(command, shell=True)

def build_Check_encoding_command(directory):
    """
    usage: 尾随空格.py [-h] [--file_extensions FILE_EXTENSIONS] --dir DIRECTORY

    检查指定目录下的文件是否存在尾随空格

    options:
    -h, --help                                 show this help message and exit
    --file_extensions FILE_EXTENSIONS          要检查的文件扩展名列表，以 , 分隔
    --dir DIRECTORY                            要检查的目录路径
    """
    file_extensions = config.get('Check_trailing_space', 'FileExtensions')
    
    if isinstance(file_extensions, list):
        file_extensions = ','.join(file_extensions)

    command = f'python 代码校对\\非UTF-8编码.py --dir {directory}'
    if file_extensions:
        command += f' --file_extensions {file_extensions}'

    subprocess.run(command, shell=True)
# ---------------------------------------------------

# -------- 调用构建函数 -----------
print("Tip:如果你看到持续一段时间没有输出可能不是卡住了，而是文件太多还没检查完，过会再看看？")
print("如果你认为确实存在异常请提交Issues。")
print(Fore.GREEN + "开始执行代码校对")
build_Check_the_trailing_space_call_command(check_directory)# 执行 代码校对\尾随空格 检查
build_Check_encoding_command(check_directory)# 执行 代码校对\非UTF-8编码 检查
print(f"{Fore.GREEN}✓{Fore.RESET} 代码校对完成！")
# --------------------------------

input("按 Enter 键退出...")
