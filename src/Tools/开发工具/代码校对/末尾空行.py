import os
import argparse
import chardet
from colorama import init, Fore

init(autoreset=True)

def check_files(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file(follow_symlinks=False):
                filepath = entry.path
                if os.access(filepath, os.R_OK):
                    try:
                        with open(filepath, 'rb') as file:
                            rawdata = file.read()
                            # 使用 chardet 库自动检测文件编码
                            result = chardet.detect(rawdata)
                            encoding = result['encoding']
                            with open(filepath, 'r', encoding=encoding) as decoded_file:
                                for line in decoded_file:
                                    last_line = line
                                if last_line:
                                    if not (last_line.endswith('\n') or last_line.endswith('\r\n')):
                                        print(f"{Fore.YELLOW}⚠{Fore.RESET} 检测到{Fore.YELLOW}末尾不是空行{Fore.RESET}: {Fore.BLUE}{filepath}{Fore.RESET}")
                                else:
                                    print(f"{Fore.RED}✕{Fore.RESET} 没有读取到末尾: {Fore.BLUE}{entry.name}{Fore.RESET}")
                    except Exception as e:
                        print(f"{Fore.RED}✕{Fore.RESET} 发生错误: {Fore.BLUE}{entry.name}{Fore.RESET}，{e}")
                else:
                    print(f"{Fore.RED}✕{Fore.RESET} 没有读取文件的权限: {Fore.BLUE}{entry.name}{Fore.RESET}，跳过检查。")
            elif entry.is_dir(follow_symlinks=False):
                # 递归遍历子目录
                check_files(entry.path)

def main(directory):
    print(f"{Fore.BLUE}[!]{Fore.RESET} 开始检查{Fore.BLUE}末尾空行{Fore.RESET}。")

    if directory:
        check_files(directory)
        print(f"{Fore.GREEN}✓{Fore.RESET} 末尾空行检查完成。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="检查文件末尾是否为空行")
    parser.add_argument("--dir", dest="directory", required=True, help="要检查的目录路径")
    args = parser.parse_args()

    # 调用主函数
    main(args.directory)
