# 标准库
# 测试阶段
import os
import shutil
import subprocess

# ---------- FOR DEV ------------
# 切记不要在开发文件夹中运行这个程序！！！
# 请先clone仓库到测试文件夹再测试！！！
# -------------------------------

# ---------- 初始初始化 -------------
os.chdir(os.path.dirname(os.path.abspath(__file__)))
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 上级目录
venv_folder_path = os.path.join(parent_dir, '.venv') # 虚拟环境目录
# -------------------------------

# ---------- 处理掉已有的虚拟环境 ---------
if os.path.exists(venv_folder_path) and os.path.isdir(venv_folder_path):
    shutil.rmtree(venv_folder_path)
    print(f"[!] 已移除旧的虚拟环境。")
# ---------------------------------------

# --------- 弄个新的 ---------
subprocess.run(['python', '-m', 'venv', venv_folder_path], check=True)
print(f"✓ 已创建新虚拟环境(venv)。")
python_exe_path = os.path.join(venv_folder_path, 'Scripts', 'python.exe')
# ---------------------------

# --------- 安装库 ---------
subprocess.run([os.path.join(venv_folder_path, 'Scripts', 'pip.exe'), 'install', 'colorama'], check=True)
subprocess.run([os.path.join(venv_folder_path, 'Scripts', 'pip.exe'), 'install', 'requests'], check=True)
# 第三方库
import requests
from colorama import init, Fore
init(autoreset=True)
# --------- 后续所需的 ↑ | 其他 ↓ ----------
# 定义多个镜像源
mirror_urls = [
    "https://pypi.tuna.tsinghua.edu.cn/simple",
    "https://mirrors.aliyun.com/pypi/simple",
    "https://pypi.mirrors.ustc.edu.cn/simple",
    "https://pypi.douban.com/simple",
    "http://pypi.hustunique.com/",
    "http://pypi.sdutlinux.org/"
]
# 测试镜像源连接速度
def test_mirror_speed(urls):
    speeds = []
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                speeds.append((url, response.elapsed.total_seconds()))
        except:
            pass
    if speeds:
        return min(speeds, key=lambda x: x[1])[0]
    else:
        return ""

# 选择速度最快的镜像源
best_mirror = test_mirror_speed(mirror_urls)

if best_mirror:
    print(f"{Fore.GREEN}✓{Fore.RESET} 最佳镜像源: {Fore.BLUE}{best_mirror}{Fore.RESET}")
else:
    print(f"{Fore.RED}✕{Fore.RESET} 无法连接任何镜像源！")
    exit()

# 更新 pip
subprocess.run([os.path.join(venv_folder_path, 'Scripts', 'python.exe'), '-m', 'pip', 'install', '--upgrade', 'pip', '--index-url', best_mirror], check=True)

# 安装所需库文件
libraries = ["translate", "beautifulsoup4", "ntplib", "tqdm", "piexif", "pyautogui", "keyboard", "configparser"]
Experimental_libraries = ["Experimental", "pygame", "pyinstaller", "nuitka", "moviepy", "plyer"]
Dev_libraries = ["chardet"]

for lib in libraries:
    print("-------------------")
    print(f"{Fore.BLUE}[!]{Fore.RESET} 正在安装库 {Fore.BLUE}{lib}{Fore.RESET}")
    subprocess.run([os.path.join(venv_folder_path, 'Scripts', 'pip.exe'), 'install', lib, '-i', best_mirror], check=True)
    print(f"{Fore.GREEN}✓{Fore.RESET} 安装库 {Fore.BLUE}{lib}{Fore.RESET} 结束")

print("-------------------")
print("是否安装仅[实验性小工具]会使用到的库？")
t = input("[Y]是 [N]否")
if t.lower == "yes" or t.lower == "y" or t.lower == "是":
    for lib in Experimental_libraries:
        print("-------------------")
        print(f"{Fore.BLUE}[!]{Fore.RESET} 正在安装库 {Fore.BLUE}{lib}{Fore.RESET}")
        subprocess.run([os.path.join(venv_folder_path, 'Scripts', 'pip.exe'), 'install', lib, '-i', best_mirror], check=True)
        print(f"{Fore.GREEN}✓{Fore.RESET} 安装库 {Fore.BLUE}{lib}{Fore.RESET} 结束")
    # --
    print("-------------------")

print("是否安装仅 开发工具 会使用到的库？")
t = input("[Y]是 [N]否")
if t.lower == "yes" or t.lower == "y" or t.lower == "是":
    for lib in Dev_libraries:
        print("-------------------")
        print(f"{Fore.BLUE}[!]{Fore.RESET} 正在安装库 {Fore.BLUE}{lib}{Fore.RESET}")
        subprocess.run([os.path.join(venv_folder_path, 'Scripts', 'pip.exe'), 'install', lib, '-i', best_mirror], check=True)
        print(f"{Fore.GREEN}✓{Fore.RESET} 安装库 {Fore.BLUE}{lib}{Fore.RESET} 结束")
    # --
    print("-------------------")

print(f"{Fore.BLUE}[!]{Fore.RESET} 安装所需库结束，请自行检查是否出错。")
# -------------------------

# -------- 让每个py/pyw文件都使用虚拟环境 ----------
for root, dirs, files in os.walk(parent_dir):
    if '环境配置' in root:
        print(f"{Fore.BLUE}[!]{Fore.RESET} 跳过 环境配置 文件夹。")
        continue  # 如果遇到名为"环境配置"的目录，直接跳过

    for filename in files:
        if filename.endswith('.py') or filename.endswith('.pyw'):
            file_path = os.path.join(root, filename)
            # 读取文件内容
            with open(file_path, 'r') as f:
                content = f.readlines()
            # 在第一行插入shebang行
            content.insert(0, '#!{}\n'.format(python_exe_path))
            # 将修改后的内容写回文件
            with open(file_path, 'w') as f:
                f.writelines(content)
            print(f"{Fore.GREEN}✓{Fore.RESET} 已将虚拟环境信息写入 {Fore.BLUE}{file_path}{Fore.RESET}")
# -------------------------------------------------
