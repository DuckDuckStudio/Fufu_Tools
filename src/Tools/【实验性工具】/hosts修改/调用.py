import os
import sys
import subprocess

# 获取当前文件的路径
current_file_path = os.path.dirname(os.path.abspath(sys.argv[0]))

# 获取当前文件所在的目录
current_dir = current_file_path.parent

# 获取需要调用的脚本文件路径
script_file_path = current_dir / "edit_hosts_file.py"
print("感谢您使用本工具来修改系统hosts文件")
print("可选操作有：")
subprocess.run(["python", script_file_path, "--help"])

while True:
    what = input("请输入你需要执行的操作：")
    if what == "-h" or what == "--help":
        subprocess.run(["python", script_file_path, "--help"])
    elif what == "--add":
        hostname = input("请输入映射的域名：")
        ip = input("请输入映射的ip：")
        subprocess.run(["python", script_file_path, "--add", ip, hostname])
        break
    elif what == "--remove":
        hostORip = input("请输入需要删除的映射ip或域名：")
        subprocess.run(["python", script_file_path, "--remove", hostORip])
        break
    elif what == "--list":
        subprocess.run(["python", script_file_path, "--list"])
        break
    else:
        print("啊哦，输入的指令似乎不正确...再试试吧！")
        print("可用指令[--add] [--remove] [--list] [-h / --help]")

input("命令执行完毕，按Enter键退出...")
