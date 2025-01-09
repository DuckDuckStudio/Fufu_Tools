import argparse
import subprocess
from colorama import init, Fore

init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description='参数查重工具')
    parser.add_argument('input', type=str, help='输入以逗号分隔的字符串')
    parser.add_argument('--show-duplicates', action='store_true', help='查找并显示重复内容')
    parser.add_argument('--remove-duplicates', action='store_true', help='查找并移除重复内容（保留一个）')
    parser.add_argument('--copy-to-clipboard', action='store_true', help='将结果复制到剪贴板（必须与--remove_duplicates同时使用）')
    args = parser.parse_args()

    if not any(vars(args).values()):
        args.remove_duplicates = True
        args.copy_to_clipboard = True

    input_string = args.input
    items = input_string.split(',')

    if args.show_duplicates:
        duplicates = {item: items.count(item) for item in set(items) if items.count(item) > 1}
        if duplicates:
            print(f'{Fore.BLUE}[!]{Fore.RESET} 重复内容为：')
            for item, count in duplicates.items():
                print(f'{item} ({Fore.BLUE}{count}{Fore.RESET}次)...')
        else:
            print(f'{Fore.GREEN}✓{Fore.RESET} 未找到重复内容')

    if args.remove_duplicates:
        unique_items = list(set(items))
        result = ','.join(unique_items)
        print(f'{Fore.GREEN}✓{Fore.RESET} 移除重复内容后的结果为：{result}')

        if args.copy_to_clipboard:
            copy_to_clipboard(result)

def copy_to_clipboard(text):
    subprocess.run('clip', input=text.encode('utf-16'), shell=True)
    print(f'{Fore.GREEN}✓{Fore.RESET} 已将结果复制到剪贴板')

if __name__ == "__main__":
    main()
