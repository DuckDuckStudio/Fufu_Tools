import os
import sys

if not sys.argv[3]: # 如果缺少3个参数中的任意一个参数，使用len(sys.argv)的话会到4
    print("[ERROR] 使用示例: python xxx.py <新版本号> <版本类型> <版本目录>")
    # 例如 python xxx.py v1.0.0 lite 打包时的目录
    sys.exit(1)

# 获取参数
新版本号 = sys.argv[1]
类型 = sys.argv[2]
目录 = sys.argv[3]

if not 新版本号:
    print("[ERROR] 新版本号不能为空")
    sys.exit(1)

if 类型 not in ['lite', 'code', 'exe', 'pack']:
    print("[ERROR] 类型必须是 lite, code, exe, pack 中的一种")
    print("[TIP] See https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/versions/ for more information.")
    sys.exit(1)

if not 目录:
    print("[ERROR] 目录不能为空")
    sys.exit(1)

# 新版本号不应以 v 开头
if 新版本号.startswith('v'):
    print("[ERROR] 新版本号不应以 v 开头")
    sys.exit(1)

print(f"[INFO] 新版本号: {新版本号}")

文件 = os.path.join(目录, "config.ini")
try:
    # 读取文件内容
    with open(文件, 'r', encoding='utf-8') as f:
        内容 = f.read()

    # 替换文本 - ini 配置文件不用带 v
    内容 = 内容.replace('major_version_number = develop', f'major_version_number = {新版本号}')

    # 写回文件
    with open(文件, 'w', encoding='utf-8') as f:
        f.write(内容)
except Exception as e:
    print(f"[ERROR] 处理 {文件} 时出错: {e}")
    sys.exit(1)

文件 = os.path.join(目录, "Version")
try:
    # 读取文件内容
    with open(文件, 'r', encoding='utf-8') as f:
        内容 = f.read()

    # 替换文本
    内容 = 内容.replace('Version: develop-code', f'Version: v{新版本号}-{类型}')

    # 写回文件
    with open(文件, 'w', encoding='utf-8') as f:
        f.write(内容)
except Exception as e:
    print(f"[ERROR] 处理 {文件} 时出错: {e}")
    sys.exit(1)

if 类型 == 'exe':
    print("[INFO] 安装程序版还需替换打包安装程序的iss文件中的版本号，接下来将开始处理。")
    文件 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))), "Installer", "Installer.iss")
    try:
        # 读取文件内容
        with open(文件, 'r', encoding='utf-8') as f:
            内容 = f.read()

        # 替换文本
        内容 = 内容.replace('develop', f'{新版本号}') # 不要替换 v

        # 写回文件
        with open(文件, 'w', encoding='utf-8') as f:
            f.write(内容)
    except Exception as e:
        print(f"[ERROR] 处理 {文件} 时出错: {e}")
        sys.exit(1)

print("[INFO] 🎉 成功处理所有文件")
sys.exit(0)
