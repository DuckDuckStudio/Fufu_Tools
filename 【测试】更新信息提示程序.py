import re
import requests
from configparser import ConfigParser

# 读取配置文件
config = ConfigParser(comment_prefixes=[])
config.read("config.ini", encoding='utf-8')
major_version = config.get('information', 'major_version_number')
sorn = config.get('information', 'status_or_revision_number')

def get_latest_version():
    try:
        response = requests.get("https://api.github.com/repos/DuckDuckStudio/Fufu_Tools/releases/latest")
        response.raise_for_status()  # 确保请求成功
        latest_version = response.json()["tag_name"]
        # 移除可能存在的v前缀
        latest_version = latest_version.lstrip('v')
        return latest_version
    except requests.RequestException as e:
        print(f"获取最新版本失败: {e}")
        return None

def parse_version(version_string):
    """解析版本号字符串，返回一个元组 (major, minor, patch, preview)"""
    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:-(\d+))?", version_string)
    if match:
        major = int(match.group(1))
        minor = int(match.group(2))
        patch = int(match.group(3))
        preview = int(match.group(4)) if match.group(4) else None
    else:
        major, minor, patch, preview = -1, -1, -1, None
    return major, minor, patch, preview

def compare_versions(version1, version2):
    """比较两个版本号，返回 1 表示第一个版本号更新，返回 0 表示版本号相同，返回 -1 表示第二个版本号更新"""
    major1, minor1, patch1, preview1 = parse_version(version1)  # 解析版本号字符串
    major2, minor2, patch2, preview2 = parse_version(version2)
    
    # 检查预览版本号是否存在，不存在则设置为0
    if preview1 is None:
        preview1 = 0
    if preview2 is None:
        preview2 = 0
    
    if major1 > major2:
        return 1
    elif major1 < major2:
        return -1
    elif minor1 > minor2:
        return 1
    elif minor1 < minor2:
        return -1
    elif patch1 > patch2:
        return 1
    elif patch1 < patch2:
        return -1
    elif preview1 > preview2:
        return 1
    elif preview1 < preview2:
        return -1
    else:
        return 0

def check_for_updates():
    current_version = major_version
    
    if not current_version:  # 如果无法获取版本号，则输出提示信息
        print("无法获取当前版本信息，请检查版本文件内容是否正确。")
        return
    
    print(f"当前版本: {current_version}")
    
    latest_version = get_latest_version()
    
    if latest_version is None:
        print("无法获取最新版本信息。")
        return
    
    print(f"最新正式版: {latest_version}")
    
    comparison_result = compare_versions(current_version, latest_version)
    
    if comparison_result < 0:
        print("发现新版本，建议更新。")
    elif comparison_result == 0:
        print("当前已是最新版本。")
    else:
        print("当前版本比最新版本更高，你认真的？")

def check_for_SORN():# SORN指status_or_revision_number，即状态或修订号
    if not sorn:
        print("[info]当前正在使用打包版")
    elif sorn == "code":
        print("[WARN]你似乎正在使用编写中的“code”版，该版本可能会出现一些意料之外的问题。")
    elif sorn == "lite":
        print("[info]当前正在使用“lite”版")
    elif sorn == "exe":
        print("[info]当前正在使用安装程序版")

check_for_updates()

check_for_SORN()

input("按Enter键继续...")
