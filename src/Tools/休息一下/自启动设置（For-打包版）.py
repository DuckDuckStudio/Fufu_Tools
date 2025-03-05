import os
import sys
import shutil

# --必要条件--
# 目标文件夹路径
startup_folder = os.path.join(os.getenv('APPDATA'), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
# 要删除的快捷方式文件名
shortcut_name = "Fufu_Tools_休息一下.lnk"
# 快捷方式文件路径
shortcut_path = os.path.join(startup_folder, shortcut_name)
# 程序所在文件夹 script_folder_with_backslash
script_folder = os.path.dirname(os.path.realpath(os.path.abspath(sys.argv[0])))
script_folder_with_backslash = script_folder + os.sep
# 源文件路径
source_file = script_folder_with_backslash + "休息一下.exe"

# 一些有趣的东西
you = 0
do = 0
what = 0

# --检查--
if os.path.exists(shortcut_path):
    # 存在
    print("休息一下工具目前已被设为自启动，是否取消设置？")
    while True :
        if you == 1 and do == 1 and what == 1:
            print("小黑子是吧！")
            you = 0
            do = 0
            what = 0
        print("[Y]是 [N]否")
        temp = input("你的回答是：")
        if temp.lower() in ["y", "yes", "是"]:
            print("删除自启动项中...")
            os.remove(shortcut_path)
            print("删除自启动项完毕！")
            break
        elif temp.lower() in ["n", "no", "否", "不"]:
            print("取消操作...")
            break
            # 退出
        elif temp.lower() in ["?","啊","？"]:
            print("问你要不要删启动项你啊什么啊？问号什么？")
            you = 0
            do = 0
            what = 0
        elif temp in ["你"]:
            print("?")
            you = 1
        elif temp in ["干"]:
            print("??")
            do = 1
        elif temp in ["嘛"]:
            print("???")
            what = 1
        else:
            you = 0
            do = 0
            what = 0
            print("请按说明回答！")
else:
    # 不存在
    print("休息一下工具目前没有被设为自启动，是否设置自启动？")
    while True :
        if you == 1 and do == 1 and what == 1:
            print("小黑子是吧！")
            you = 0
            do = 0
            what = 0
        print("[Y]是 [N]否")
        temp = input("你的回答是：")
        if temp.lower() in ["y", "yes", "是"]:
            print("创建自启动项中...")
            # 在启动文件夹中创建快捷方式
            shutil.copyfile(source_file, shortcut_path)
            print("创建自启动项完毕！")
            break
        elif temp.lower() in ["n", "no", "否", "不"]:
            print("取消操作...")
            break
            # 退出
        elif temp.lower() in ["?","啊","？"]:
            print("问你要不要加启动项你啊什么啊？问号什么？")
            you = 0
            do = 0
            what = 0
        elif temp in ["你"]:
            print("?")
            you = 1
        elif temp in ["干"]:
            print("??")
            do = 1
        elif temp in ["嘛"]:
            print("???")
            what = 1
        else:
            you = 0
            do = 0
            what = 0
            print("请按说明回答！")

input("按Enter键继续...")