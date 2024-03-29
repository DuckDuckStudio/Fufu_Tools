import os

# 更新 pip
os.system(f"python -m pip install --upgrade pip")

# 安装所需库文件
libraries = ["translate", "requests", "beautifulsoup4", "ntplib", "tqdm", "piexif", "pyautogui", "keyboard"]

for lib in libraries:
    print("-------------------")
    print(f"正在安装库 {lib}")
    os.system(f"pip install {lib}")
    print(f"安装库 {lib} 结束")

print("-------------------")
print("所有所需库文件安装完成！")
print("错误关键词ERROR，如有看到请确认库文件安装情况。")
print("如果看不懂可以使用翻译软件！")
input("按任意键继续...")