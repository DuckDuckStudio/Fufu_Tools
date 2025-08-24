import os
import sys
from tqdm import tqdm
import subprocess
import configparser

# READ config.ini file
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
config_file_path = os.path.join(script_dir, "config.ini")
config = configparser.ConfigParser()
config.read(config_file_path)
ctr = config.get('settings', 'customer_temp_folder')
ac_ctr = config.getboolean('settings', 'always_clear_ctr')

print("正在删除缓存文件...")

temp_path = os.environ["TEMP"]
username = os.environ["USERNAME"]
local_temp_path = f"C:\\Documents and Settings\\{username}\\Local Settings\\temp"
tmp_path = os.environ["TMP"]

# 获取所有缓存文件路径
file_paths: list[str] = []

# -- Check --
if ctr == "False":
    flag = False
else:
    flag = True

if flag:# 有任意值且不为False则为True
    print("检测到自定义缓存文件夹，是否同步清理？")
    while not ac_ctr:
        print("[Y]是 [N]否 [A]总是")
        temp = input("你的回答是：")
        if temp.lower() in ["y", "yes", "是"]:
            for root, dirs, files in os.walk(ctr):
                for file in files:
                    file_paths.append(os.path.join(root, file))
            break
        elif temp.lower() in ["a", "always", "总是"]:
            print("设置中...")
            # 修改ini文件配置
            config["settings"]["always_clear_ctr"] = "True"
            with open(config_file_path, 'w') as configfile:
                config.write(configfile)
            print("设置完成！")
            break
        else:
            # elif temp.lower() in ["n", "no", "否", "不"]:
            break
    if ac_ctr:
        for root, dirs, files in os.walk(ctr):
            for file in files:
                file_paths.append(os.path.join(root, file))


for root, dirs, files in os.walk(temp_path):
    for file in files:
        file_paths.append(os.path.join(root, file))
for root, dirs, files in os.walk(local_temp_path):
    for file in files:
        file_paths.append(os.path.join(root, file))
for root, dirs, files in os.walk(tmp_path):
    for file in files:
        file_paths.append(os.path.join(root, file))

total_files = len(file_paths)

# 使用tqdm显示进度条
with tqdm(total=total_files, ncols=80) as pbar:
    for file_path in file_paths:
        try:
            os.remove(file_path)
        except PermissionError:
            pass
        except OSError:
            pass
        finally:
            pbar.update(1)
print("缓存文件删除完成！")
#  对于TEMP ↑  对于Windows.old ↓

windows_old_path = 'C:\\windows.old'

if os.path.isdir(windows_old_path):
    print("检测到之前的Windows文件，在不需要回退到旧版本Windows的情况下可以安全删除。")
    print("详细信息请查看Microsoft支持：https://support.microsoft.com/zh-cn/windows/删除以前版本的-windows-f8b26680-e083-c710-b757-7567d69dbb74")
    print("是否删除之前的Windows文件？")
    print("[Y]是 [N]否")
    temp = input("你的回答是：")
    if temp.lower() in ["y", "yes", "是"]:
        print("正在尝试打开存储设置...请点击临时文件分类并手动删除...")
        subprocess.run("start ms-settings:storagesense", shell=True)
        # Windows好像没有让程序直接打开临时文件分类的URI
        # 如果直接尝试删除windows.old将会遇到“拒绝访问”等权限错误...
            
input("按Enter键继续...")
