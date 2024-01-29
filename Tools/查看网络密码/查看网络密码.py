import os

def main():
    os.system('netsh wlan show profiles')
    wifi_name = input("请输入你要查询的wifi名：")
    os.system(f'netsh wlan show profile name="{wifi_name}" key=clear')
    print()
    input_str = input("你还想查询其他wifi吗？（y/n）")
    if input_str == 'y':
        main()
    elif input_str == 'n':
        input("按任意键退出...")
    else:
        print("输入有误，程序已退出。")

if __name__ == '__main__':
    main()
