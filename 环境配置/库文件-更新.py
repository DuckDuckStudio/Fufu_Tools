import os

# 更新 pip
os.system(f"python -m pip install --upgrade pip")

# 更新所需库文件
libraries = ["translate", "requests", "beautifulsoup4", "ntplib", "tqdm", "piexif", "pyautogui", "keyboard", "configparser"]
Experimental_libraries = ["Experimental", "pygame", "pyinstaller", "nuitka", "moviepy", "plyer"]
Dev_libraries = ["chardet"]

for lib in libraries:
    print("-------------------")
    print(f"正在更新库 {lib}")
    os.system(f"pip install --upgrade {lib}")
    print(f"更新库 {lib} 结束")

print("-------------------")
print("是否更新仅[实验性小工具]会使用到的库？")
t = input("[Y]是 [N]否")
if t.lower == "yes" or t.lower == "y" or t.lower == "是":
    for lib in Experimental_libraries:
        print("-------------------")
        print(f"正在更新库 {lib}")
        os.system(f"pip install --upgrade {lib}")
        print(f"更新库 {lib} 结束")
    # --
    print("-------------------")

print("是否更新仅 开发工具 会使用到的库？")
t = input("[Y]是 [N]否")
if t.lower == "yes" or t.lower == "y" or t.lower == "是":
    for lib in Dev_libraries:
        print("-------------------")
        print(f"正在更新库 {lib}")
        os.system(f"pip install --upgrade {lib}")
        print(f"更新库 {lib} 结束")
    # --
    print("-------------------")

print("所有所需库文件更新完成！")
print("错误关键词ERROR，如有看到请确认库文件更新情况。")
print("如果看不懂可以使用翻译软件！")
input("按任意键继续...")