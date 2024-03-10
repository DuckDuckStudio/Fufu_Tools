import os
import configparser

print("读取config.ini文件中...")
# READ config.ini file
script_dir = os.path.dirname(os.path.realpath(__file__))
config_file_path = os.path.join(script_dir, "config.ini")
config = configparser.ConfigParser()
config.read(config_file_path)

print("写入中...")
# 修改ini文件配置
config["settings"]["always_open_more_info"] = "False"
with open(config_file_path, 'w') as configfile:
    config.write(configfile)

print("设置完成！")