import os
import argparse
import chardet
from colorama import init, Fore
init(autoreset=True)

def check_files(directory, file_extensions):
    """
    检查指定目录下的文件是否存在非UTF-8编码的文件。

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
                                if encoding != 'utf-8':
                                    print(f"{Fore.YELLOW}⚠{Fore.RESET} 文件编码可能不是UTF-8: {Fore.BLUE}{entry.name}{Fore.RESET}，依据内容猜测编码为 {Fore.BLUE}{encoding}{Fore.RESET}")
                        except Exception as e:
                            print(f"{Fore.RED}✕{Fore.RESET} 发生错误: {Fore.BLUE}{entry.name}{Fore.RESET}，{e}")
                    else:
                        print(f"{Fore.RED}✕{Fore.RESET} 没有读取文件的权限: {Fore.BLUE}{entry.name}{Fore.RESET}，跳过检查。")
            elif entry.is_dir(follow_symlinks=False):
                # 递归遍历子目录
                check_files(entry.path)

def main(directory, file_extensions):
    print(f"{Fore.BLUE}[!]{Fore.RESET} 开始进行{Fore.BLUE}编码检查{Fore.RESET}。")

    # 检查文件
    if directory:
        check_files(directory, file_extensions)
        print(f"{Fore.GREEN}✓{Fore.RESET} 编码检查完成。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="检查指定目录下的文件是否存在非UTF-8编码的文件")
    parser.add_argument("--file_extensions", dest="file_extensions", type=str, help="要检查的文件扩展名列表，以 , 分隔")
    parser.add_argument("--dir", dest="directory", required=True, help="要检查的目录路径")
    args = parser.parse_args()

    # 将逗号分隔的字符串转换为列表
    file_extensions = args.file_extensions.split(',') if args.file_extensions else []

    # 调用主函数
    main(args.directory, file_extensions)
