import os
import sys
import json
import subprocess
import argparse
from colorama import init, Fore

init(autoreset=True)

def switch_git_config(alias, fast_switch=False, switch_name=True, switch_email=True):
    is_global = subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode != 0
    
    config_scope = '--global' if is_global else '--local'
    # 全局 或 本地 | 系统 > 全局 > 本地
    scope_msg = "全局配置" if is_global else "配置仅限于本仓库目录"
    print(f"\r{Fore.BLUE}[!]{Fore.RESET} {scope_msg}")

    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    accounts_file = os.path.join(script_dir, 'accounts.json')
    
    # 读取账号信息
    with open(accounts_file, 'r', encoding='utf-8') as file:
        accounts = json.load(file)
    
    # 检查是否存在提供的别名
    if fast_switch:
        matched_users = [user for user, info in accounts.items() if alias in info.get('aliases', [])]
        if not matched_users:
            print(f'{Fore.RED}✕{Fore.RESET} 在accounts.json中未找到与"{alias}"匹配的用户')
            return 1
        if len(matched_users) > 1:
            print(f'{Fore.RED}✕{Fore.RESET} 在accounts.json中找到多个与"{alias}"匹配的用户：{", ".join(matched_users)}。请提供更具体的别名。')
            return 1
    else:
        name_users = [user for user, info in accounts.items() if alias == info.get('name')]
        if not name_users:
            print(f'{Fore.RED}✕{Fore.RESET} 在accounts.json中未找到与"{alias}"匹配的用户')
            print(f'{Fore.BLUE}[!]{Fore.RESET} 提示：如需使用别名请添加{Fore.BLUE}--fast{Fore.RESET}参数。')
            return 1
        if len(name_users) > 1:
            print(f'{Fore.RED}✕{Fore.RESET} 在accounts.json中找到多个与"{alias}"匹配的用户：{", ".join(matched_users)}。请提供更具体的别名。')
            return 1
    
    user_info = accounts[matched_users[0]]
    
    # 设置Git配置
    if switch_name:
        result = subprocess.run(['git', 'config', config_scope, 'user.name', user_info['name']])
        if result.returncode == 0:
            print(f'{Fore.GREEN}✓{Fore.RESET} 已切换Git用户名：{user_info["name"]}')
        else:
            print(f'{Fore.RED}✕{Fore.RESET} 切换失败: {Fore.RED}{result.stderr}{Fore.RESET}')
            return 1
    if switch_email:
        result = subprocess.run(['git', 'config', config_scope, 'user.email', user_info['email']])
        if result.returncode == 0:
            print(f'{Fore.GREEN}✓{Fore.RESET} 已切换Git邮箱：{user_info["email"]}')
        else:
            print(f'{Fore.RED}✕{Fore.RESET} 切换失败: {Fore.RED}{result.stderr}{Fore.RESET}')
            return 1
    return 0

def edit_json_file(script_dir):
    accounts_file = os.path.join(script_dir, 'accounts.json')
    
    try:
        os.startfile(accounts_file)
        return 0
    except Exception as e:
        print(f'{Fore.RED}✕{Fore.RESET} 打开数据文件失败:\n{Fore.RED}{e}{Fore.RESET}\n{Fore.BLUE}[!]{Fore.RESET} 您可以手动打开 {Fore.BLUE}{accounts_file}{Fore.RESET}')
        return 1

def show_git_config():
    result = subprocess.run(['git', 'config', 'user.name'], capture_output=True, text=True)
    if result.returncode == 0:
        print(f'{Fore.GREEN}✓{Fore.RESET} 已设置Git用户名: {result.stdout.strip()}')
    else:
        print(f'{Fore.RED}✕{Fore.RESET} 查看用户名配置失败: {Fore.RED}{result.stderr.strip()}{Fore.RESET}')
        return 1
    result = subprocess.run(['git', 'config', 'user.email'], capture_output=True, text=True)
    if result.returncode == 0:
        print(f'{Fore.GREEN}✓{Fore.RESET} 已设置Git邮箱: {result.stdout.strip()}')
    else:
        print(f'{Fore.RED}✕{Fore.RESET} 查看邮箱配置失败: {Fore.RED}{result.stderr.strip()}{Fore.RESET}')
        return 1
    return 0

def main():
    parser = argparse.ArgumentParser(description='账号切换')
    parser.add_argument('--fast', action='store_true', help='快速切换模式')
    parser.add_argument('--edit', action='store_true', help='编辑 accounts.json 文件')
    parser.add_argument('--show', action='store_true', help='显示现有配置')
    parser.add_argument('--name', action='store_true', help='仅切换 Git 用户名')
    parser.add_argument('--email', action='store_true', help='仅切换 Git 邮箱')
    parser.add_argument('alias', metavar='ALIAS', type=str, nargs='?', help='用户名/别名')
    
    args = parser.parse_args()
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    
    if args.edit:
        return(edit_json_file(script_dir))
    elif args.show:
        return(show_git_config())
    elif args.alias:
        switch_name = not args.email # 如果未提供 --email 参数，切换用户名
        switch_email = not args.name # 如果未提供 --name 参数，切换邮箱
        return(switch_git_config(args.alias, args.fast, switch_name, switch_email))
    else:
        print(f"{Fore.RED}✕{Fore.RESET} 请提供一个别名或者使用 --edit 参数来编辑 accounts.json 文件")
        return 1
    # 每个判断都有 return 了这里就不用加

if __name__ == "__main__":
    sys.exit(main())
