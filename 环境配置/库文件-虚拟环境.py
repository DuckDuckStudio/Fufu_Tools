#!..\.venv\Script\python.exe
import os
import subprocess
import requests
from colorama import init, Fore
init(autoreset=True)
# ---------- 初始化 -------------
os.chdir(os.path.dirname(os.path.abspath(__file__)))
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 上级目录
venv_folder_path = os.path.join(parent_dir, '.venv') # 虚拟环境目录
python_exe_path = os.path.join(venv_folder_path, 'Scripts', 'python.exe')
# -------------------------------

# 定义多个镜像源
mirror_urls = [
    "https://pypi.org/simple",# 默认源
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
    print(f"{Fore.GREEN}✓{Fore.RESET} 最佳源: {Fore.BLUE}{best_mirror}{Fore.RESET}")
else:
    print(f"{Fore.RED}✕{Fore.RESET} 无法连接任何镜像源！")
    exit()

# 更新 pip
subprocess.run([os.path.join(venv_folder_path, 'Scripts', 'python.exe'), '-m', 'pip', 'install', '--upgrade', 'pip', '--index-url', best_mirror], check=True)

# 安装所需库文件
libraries = ["translate", "beautifulsoup4", "ntplib", "tqdm", "piexif", "pyautogui", "keyboard", "configparser", "pyshortcuts"]
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