import os
import argparse
import configparser
from colorama import init, Fore

init(autoreset=True)

def count_lines_in_file(file_path, ignore_empty_lines=False, ignore_comments=False, show_ignored_lines=False, show_test_info=False):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            if show_test_info:
                print(f"{Fore.YELLOW}[TEST]{Fore.RESET} {Fore.GREEN}正在{Fore.RESET}处理文件 {Fore.BLUE}{file_path}{Fore.RESET}")
            lines = file.readlines()
            if ignore_empty_lines:
                original_line_count = len(lines)
                lines = [line for line in lines if line.strip()]
                ignored_empty_lines = original_line_count - len(lines)
            else:
                ignored_empty_lines = 0
            if ignore_comments:
                original_line_count = len(lines)
                lines = [line for line in lines if not line.strip().startswith('#')]
                ignored_comment_lines = original_line_count - len(lines)
            else:
                ignored_comment_lines = 0
            total_lines = len(lines)
            if show_ignored_lines:
                return total_lines, ignored_empty_lines, ignored_comment_lines
            return total_lines
    except FileNotFoundError:
        print(f"{Fore.RED}✕{Fore.RESET} 文件不存在: {Fore.BLUE}{file_path}{Fore.RESET}")
        return 0, 0, 0
    except PermissionError:
        print(f"{Fore.RED}✕{Fore.RESET} 没有权限访问文件: {Fore.BLUE}{file_path}{Fore.RESET}")
        return 0, 0, 0
    except Exception as e:
        print(f"{Fore.RED}✕{Fore.RESET} 文件 {Fore.BLUE}{file_path}{Fore.RESET} 出现未知错误: {Fore.RED}{e}{Fore.RESET}")
        return 0, 0, 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='计算指定目录中的总代码行数')
    parser.add_argument('--dir', help='要扫描的目录', required=True, dest="dir_path")
    parser.add_argument('--ignore-folders', help='要忽略的文件夹（逗号分隔）', required=False, dest="ignore_folders")
    parser.add_argument('--ignore-files', help='要忽略的文件（逗号分隔）', required=False, dest="ignore_files")
    parser.add_argument('--formats', help='要包含的文件格式（逗号分隔）', required=False, dest="file_formats")
    parser.add_argument('--ignore-empty-lines', action='store_true', help='在统计时忽略空行', required=False, dest="ignore_empty_lines")
    parser.add_argument('--ignore-comments', action='store_true', help='在统计时忽略注释行', required=False, dest="ignore_comments")
    parser.add_argument('--show-ignored-lines', action='store_true', help='显示总共忽略的空行和注释行数', required=False, dest="show_ignored_lines")
    parser.add_argument('--show-test-info', action='store_true', help='显示测试信息（非必要不要使用）', required=False, dest="show_test_info")
    parser.add_argument('--code-file-formats', action='store_true', help='仅统计代码文件', required=False, dest="code_file_formats")

    args = parser.parse_args()

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    config = configparser.ConfigParser()
    config.read('..\\config.ini')
    code_file_extensions = config.get('Statistics', 'CodeFileExtensions')

    ignore_folders = args.ignore_folders.split(',') if args.ignore_folders else []
    ignore_files = args.ignore_files.split(',') if args.ignore_files else []

    if args.file_formats and args.code_file_formats:
        print(f"{Fore.RED}✕{Fore.RESET} --formats 不得与 --code-file-formats 同时使用")
        exit()
    elif args.file_formats:
        file_formats = args.file_formats.split(',')
    elif args.code_file_formats:
        file_formats = code_file_extensions.split(',')
    else:
        file_formats = []

    total_lines = 0
    ignored_empty_lines = 0
    ignored_comment_lines = 0

    if not os.path.exists(args.dir_path):
        print(f"{Fore.RED}✕{Fore.RESET} 指定的目录不存在")
        exit()

    for root, dirs, files in os.walk(args.dir_path):
        dirs[:] = [d for d in dirs if d not in ignore_folders]
        for file in files:
            if file not in ignore_files:
                if args.show_test_info:
                    print(f"{Fore.YELLOW}[TEST]{Fore.RESET} 文件 {Fore.BLUE}{file}{Fore.RESET} {Fore.GREEN}未被{Fore.YELLOW}忽略文件{Fore.RESET}参数忽略")
                if not file_formats or file.endswith(tuple(file_formats)):
                    if args.show_test_info:
                        print(f"{Fore.YELLOW}[TEST]{Fore.RESET} 文件 {Fore.BLUE}{file}{Fore.RESET} {Fore.GREEN}未被{Fore.YELLOW}指定格式{Fore.RESET}参数忽略 ({not args.file_formats} | {file.endswith(tuple(file_formats))})")
                    file_path = os.path.join(root, file)
                    lines = count_lines_in_file(file_path, args.ignore_empty_lines, args.ignore_comments, args.show_ignored_lines, args.show_test_info)
                    if args.show_ignored_lines:
                        total_lines += lines[0]
                        ignored_empty_lines += lines[1]
                        ignored_comment_lines += lines[2]
                    else:
                        total_lines += lines

    print(f'{Fore.GREEN}✓{Fore.RESET} 总代码行数: {total_lines} 行')
    if args.show_ignored_lines:
        ignored_lines = 0
        if args.ignore_empty_lines:
            print(f'{Fore.BLUE}[!]{Fore.RESET} 总共忽略的空行数: {ignored_empty_lines} 行')
            ignored_lines += ignored_empty_lines
        if args.ignore_comments:
            print(f'{Fore.BLUE}[!]{Fore.RESET} 总共忽略的注释行数: {ignored_comment_lines} 行')
            ignored_lines += ignored_comment_lines
        print(f'{Fore.BLUE}[!]{Fore.RESET} 总共忽略了: {ignored_lines} 行')
