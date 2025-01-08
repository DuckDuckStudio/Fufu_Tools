import os
import sys

# GitHub Action - Windows 竟然只能输出英文 :(

if len(sys.argv) != 3:
    print("[ERROR] Usage: python xxx.py <New-version> <Type>")
    # 例如 python xxx.py v1.0.0 lite
    sys.exit(1)

# 获取参数
新版本号 = sys.argv[1]
类型 = sys.argv[2]

if not 新版本号:
    print("[ERROR] Version cannot be empty.")
    sys.exit(1)

if 类型 not in ['lite', 'code', 'exe', 'pack']:
    print("[ERROR] Type must be one of 'lite', 'code', 'exe', 'pack'.")
    print("[TIP] See https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/versions/ for more information.")
    sys.exit(1)

# 如果新版本号以 v 开头，去掉 v
if 新版本号.startswith('v'):
    新版本号 = 新版本号[1:] # 切片
    print("[WARNING] The version number should NOT start with 'v', it will be automatically removed.")

print(f"[INFO] New version: {新版本号}")

文件 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))), "src", "config.ini")
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
    print(f"[ERROR] A error occurred when processing {文件}: {e}")
    sys.exit(1)

文件 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))), "src", "Version")
try:
    # 读取文件内容
    with open(文件, 'r', encoding='utf-8') as f:
        内容 = f.read()

    # 替换文本
    内容 = 内容.replace('Version: develop-code', f'Version: v{新版本号}-code')

    # 写回文件
    with open(文件, 'w', encoding='utf-8') as f:
        f.write(内容)
except Exception as e:
    print(f"[ERROR] A error occurred when processing {文件}: {e}")
    sys.exit(1)

# 请勿使用表情，GitHub Action 会有意见的 :(
print("[INFO] Version number processing is complete for all files!")
sys.exit(0)
