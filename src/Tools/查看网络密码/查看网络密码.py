import subprocess

def main():
    subprocess.run(["netsh", "wlan", "show", "profiles"], check=True)
    wifi_name = input("请输入你要查询的wifi名：")
    subprocess.run(["netsh", "wlan", "show", "profile", f"name={wifi_name}", "key=clear"], check=True)
    print()
    input_str = input("你还想查询其他wifi吗？（y/n）")
    if input_str == "y":
        main()
    elif input_str == "n":
        print("取消操作...")
    else:
        print("输入有误，程序已退出。")

if __name__ == "__main__":
    main()

input("按Enter键继续...")
