import os
import configparser

# READ config.ini file
script_dir = os.path.dirname(os.path.realpath(__file__))
config_file_path = os.path.join(script_dir, "config.ini")
config = configparser.ConfigParser()
config.read(config_file_path)
mvn = config.get('information', 'major_version_number')
sorn = config.get('information', 'status_or_revision_number')

# output
print("--------------芙芙工具箱--------------")
print("-> Code by 鸭鸭「カモ」/ DuckStudio")
print(f"Version: v{mvn}-{sorn}")
print("-------------------------------------")