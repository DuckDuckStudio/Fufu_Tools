import os
import sys
import json
import subprocess

# ---- HELP INFO ----
# usage: 账号切换.py [--fast] USERNAME
# ---- --------- ----

def switch_git_config(alias, fast_switch=False):
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
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
    subprocess.run(['git', 'config', 'user.name', user_info['name']])
    subprocess.run(['git', 'config', 'user.email', user_info['email']])
    print(f'已切换到Git用户：{user_info["name"]} ({user_info["email"]})')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python 账号切换.py [--fast] <用户名/别名>")
        sys.exit(1)
    
    fast_switch = False
    alias = None
    
    # 检查是否提供了--fast参数
    if "--fast" in sys.argv:
        fast_switch = True
        username_index = sys.argv.index("--fast") + 1
    else:
        username_index = 1
    
    # 获取别名
    if username_index < len(sys.argv):
        alias = sys.argv[username_index]
    else:
        print("错误：请提供一个别名")
        sys.exit(1)
    
    switch_git_config(alias, fast_switch)
