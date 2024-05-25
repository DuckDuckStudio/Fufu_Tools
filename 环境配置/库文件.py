import os

print("-------------------")
print(f"正在安装库 requests")
os.system(f"pip install requests")
print(f"安装库 requests 结束")
print("-------------------")
# 必须的库，否则检测不起作用

import requests

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
    print(f"最佳源：{best_mirror}")
else:
    print("无法连接任何镜像源！")

# 更新 pip
os.system(f"python -m pip install --upgrade pip --index-url {best_mirror}")

# 安装所需库文件
libraries = ["translate", "beautifulsoup4", "ntplib", "tqdm", "piexif", "pyautogui", "keyboard", "configparser", "pyshortcuts"]
Experimental_libraries = ["Experimental", "pygame", "pyinstaller", "nuitka", "moviepy", "plyer"]
Dev_libraries = ["chardet"]

for lib in libraries:
    print("-------------------")
    print(f"正在安装库 {lib}")
    os.system(f"pip install {lib} -i {best_mirror}")
    print(f"安装库 {lib} 结束")

print("-------------------")
print("是否安装仅[实验性小工具]会使用到的库？")
t = input("[Y]是 [N]否")
if t.lower == "yes" or t.lower == "y" or t.lower == "是":
    for lib in Experimental_libraries:
        print("-------------------")
        print(f"正在安装库 {lib}")
        os.system(f"pip install {lib} -i {best_mirror}")
        print(f"安装库 {lib} 结束")
    # --
    print("-------------------")

print("是否安装仅 开发工具 会使用到的库？")
t = input("[Y]是 [N]否")
if t.lower == "yes" or t.lower == "y" or t.lower == "是":
    for lib in Dev_libraries:
        print("-------------------")
        print(f"正在安装库 {lib}")
        os.system(f"pip install {lib} -i {best_mirror}")
        print(f"安装库 {lib} 结束")
    # --
    print("-------------------")

print("所有所需库文件安装完成！")
print("错误关键词ERROR，如有看到请确认库文件安装情况。")
print("如果看不懂可以使用翻译软件！")
input("按任意键继续...")
