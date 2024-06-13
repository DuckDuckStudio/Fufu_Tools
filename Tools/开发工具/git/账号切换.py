import os
import sys
import json
import subprocess
import argparse

def switch_git_config(alias, fast_switch=False, switch_name=True, switch_email=True):
    accounts_file = os.path.join(script_dir, 'accounts.json')
    
    # 读取账号信息
    with open(accounts_file, 'r', encoding='utf-8') as file:
        accounts = json.load(file)
    
    # 检查是否存在提供的别名
    if fast_switch:
        matched_users = [user for user, info in accounts.items() if alias in info.get('aliases', [])]
        if not matched_users:
            print(f'错误：在accounts.json中未找到与"{alias}"匹配的用户')
            return
        if len(matched_users) > 1:
            print(f'错误：在accounts.json中找到多个与"{alias}"匹配的用户：{", ".join(matched_users)}。请提供更具体的别名。')
            return
    else:
        name_users = [user for user, info in accounts.items() if alias == info.get('name')]
        if not name_users:
            print(f'错误：在accounts.json中未找到与"{alias}"匹配的用户')
            print(f'提示：如需使用别名请添加--fast参数。')
            return
        if len(name_users) > 1:
            print(f'错误：在accounts.json中找到多个与"{alias}"匹配的用户：{", ".join(matched_users)}。请提供更具体的别名。')
            return
    
    user_info = accounts[matched_users[0]]
    
    # 设置Git配置
    if switch_name:
        subprocess.run(['git', 'config', 'user.name', user_info['name']])
        print(f'已切换Git用户名：{user_info["name"]}')
    if switch_email:
        subprocess.run(['git', 'config', 'user.email', user_info['email']])
        print(f'已切换Git邮箱：{user_info["email"]}')

def edit_json_file():
    accounts_file = os.path.join(script_dir, 'accounts.json')
    
    try:
        os.startfile(accounts_file)
    except AttributeError:
        subprocess.run(['open', accounts_file])  # macOS
    except:
        subprocess.run(['xdg-open', accounts_file])  # Linux

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='账号切换')
    parser.add_argument('--fast', action='store_true', help='快速切换模式')
    parser.add_argument('--edit', action='store_true', help='编辑 accounts.json 文件')
    parser.add_argument('--name', action='store_true', help='仅切换 Git 用户名')
    parser.add_argument('--email', action='store_true', help='仅切换 Git 邮箱')
    parser.add_argument('alias', metavar='ALIAS', type=str, nargs='?', help='用户名/别名')
    
    args = parser.parse_args()
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    
    if args.edit:
        edit_json_file()
    elif args.alias:
        switch_name = not args.email  # 如果未提供 --email 参数，切换用户名
        switch_email = not args.name  # 如果未提供 --name 参数，切换邮箱
        switch_git_config(args.alias, args.fast, switch_name, switch_email)
    else:
        print("错误：请提供一个别名或者使用 --edit 参数来编辑 accounts.json 文件")
        sys.exit(1)
