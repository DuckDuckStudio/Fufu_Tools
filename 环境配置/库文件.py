import os

# 更新 pip
os.system(f"python -m pip install --upgrade pip")

# 安装所需库文件
libraries = ["translate", "requests", "beautifulsoup4", "ntplib", "tqdm", "piexif", "pyautogui", "keyboard"]
Experimental_libraries = ["Experimental", "pygame", "pyinstaller", "nuitka", "moviepy", "plyer"]

for lib in libraries:
    print("-------------------")
    print(f"正在安装库 {lib}")
    os.system(f"pip install {lib}")
    print(f"安装库 {lib} 结束")

print("-------------------")
print("是否安装仅[实验性小工具]会使用到的库？")
t = input("[Y]是 [N]否")
if t.lower == "yes" or t.lower == "y" or t.lower == "是":
    for lib in Experimental_libraries:
        print("-------------------")
        print(f"正在安装库 {lib}")
        os.system(f"pip install {lib}")
        print(f"安装库 {lib} 结束")
    # --
    print("-------------------")

print("所有所需库文件安装完成！")
print("错误关键词ERROR，如有看到请确认库文件安装情况。")
print("如果看不懂可以使用翻译软件！")
input("按任意键继续...")