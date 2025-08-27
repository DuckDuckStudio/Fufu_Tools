import os
import sys
import configparser

def main():
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    config_file_path = os.path.join(script_dir, "config.ini")
    config = configparser.ConfigParser()
    config.read(config_file_path)
    mvn = config.get("information", "major_version_number")
    sorn = config.get("information", "status_or_revision_number")

    # TODO: 这还不如用弹窗显示...
    print("--------------芙芙工具箱--------------")
    print("-> Code by 鸭鸭「カモ」/ DuckStudio")
    print(f"Version: v{mvn}-{sorn}")
    print("-------------------------------------")

    input("按 Enter 键继续...")


if __name__ == "__main__":
    main()
