import os
import re
import argparse
import chardet
from colorama import init, Fore

def check_files(directory, file_extensions=None):
    """
    检查指定目录下的文件是否存在尾随空格。

    Args:
    - directory: 要检查的目录路径。
    - file_extensions: 要检查的文件扩展名列表。如果为空，则检查所有文件。
    """
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file(follow_symlinks=False):
                if not file_extensions or entry.name.endswith(tuple(file_extensions)):
                    filepath = entry.path
                    if os.access(filepath, os.R_OK):
                        try:
                            with open(filepath, 'rb') as file:
                                rawdata = file.read()
                                # 使用 chardet 库自动检测文件编码
                                result = chardet.detect(rawdata)
                                encoding = result['encoding']
                                with open(filepath, 'r', encoding=encoding) as decoded_file:
                                    linenum = 0
                                    for line in decoded_file:
                                        linenum += 1
                                        # 使用正则表达式检查行尾是否包含空格，但不以换行符结尾
                                        if re.search(r'[^\S\n]$', line):
                                            if line.isspace():
                                                print(f"{Fore.YELLOW}⚠{Fore.RESET} 检测到{Fore.YELLOW}多余空行空格{Fore.RESET}: {Fore.BLUE}{filepath}{Fore.RESET}, 第 {Fore.BLUE}{linenum}{Fore.RESET} 行。")
                                            else:
                                                print(f"{Fore.YELLOW}⚠{Fore.RESET} 检测到{Fore.YELLOW}尾随空格{Fore.RESET}: {Fore.BLUE}{filepath}{Fore.RESET}, 第 {Fore.BLUE}{linenum}{Fore.RESET} 行。")
                        except Exception as e:
                            print(f"{Fore.RED}✕{Fore.RESET} 发生错误: {Fore.BLUE}{filepath}{Fore.RESET}，{e}")
                    else:
                        print(f"{Fore.RED}✕{Fore.RESET} 没有读取文件的权限: {Fore.BLUE}{filepath}{Fore.RESET}，跳过检查。")
            elif entry.is_dir(follow_symlinks=False):
                # 递归遍历子目录
                check_files(entry.path)

def main(directory, file_extensions=None):
    init(autoreset=True)

    print(f"{Fore.BLUE}[!]{Fore.RESET} 开始检查{Fore.BLUE}尾随空格{Fore.RESET}。")

    # 检查文件
    if directory:
        check_files(directory, file_extensions)
        print(f"{Fore.GREEN}✓{Fore.RESET} 尾随空格检查完成。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="检查指定目录下的文件是否存在尾随空格")
    parser.add_argument("--file_extensions", dest="file_extensions", type=str, help="要检查的文件扩展名列表，以 , 分隔")
    parser.add_argument("--dir", dest="directory", required=True, help="要检查的目录路径")
    args = parser.parse_args()

    if args.file_extensions:
        # 将逗号分隔的字符串转换为列表
        file_extensions = args.file_extensions.split(',') if args.file_extensions else []
        main(args.directory, file_extensions)
    else:
        main(args.directory)
