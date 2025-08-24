import os
import sys
import configparser

# READ config.ini file
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
config_file_path = os.path.join(script_dir, "config.ini")
FRDC_file_path = os.path.join(script_dir, "fast_return_default_config.py")
config = configparser.ConfigParser()
config.read(config_file_path)
always_open = config.getboolean("settings", "always_open_more_info")

print("您的设备信息如下：")
# 执行 systeminfo 命令并输出结果
os.system("systeminfo")

# --检查--
# 通过读取config.ini文件来获取是否总是显示
if always_open:
    # set flag
    flag = False
    print("已设置总是显示详细信息，启动页面中...")
    os.system("msinfo32")
    print("已展示，请查看弹出的窗口")
else:
    flag = True
# 本应在ini文件中的注释：
# ; always_open_more_info set
# ; True -> always
# ; False -> ask (default)

if flag:
    print("是否查看更详细的信息？")
    print("[Y]是 [N]否 [A]总是")
    temp = input("你的回答是：")

    if temp.lower() in ["y", "yes", "是"]:
        print("启动页面中...")
        os.system("msinfo32")
        print("已展示，请查看弹出的窗口")
    elif temp.lower() in ["a", "always", "总是"]:
        print("设置中...")
        # 修改ini文件配置
        config["settings"]["always_open_more_info"] = "True"
        with open(config_file_path, "w") as configfile:
            config.write(configfile)
        print("设置完成！")

        print("启动页面中...")
        os.system("msinfo32")
        print("已展示，请查看弹出的窗口")
    else:
        print("取消操作...")

input("按Enter键继续...")
