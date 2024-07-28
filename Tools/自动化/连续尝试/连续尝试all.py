import os
import time
import subprocess
from plyer import notification
from colorama import init, Fore

# --- init ---
init(autoreset=True)
# ------------

def run_command(command): # 执行命令
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        return "Successful"
    else:
        return result.stderr

def main():
    user_input = input(f"{Fore.BLUE}?{Fore.RESET} 请输入你需要执行的命令:")

    while True:
        route = input(f"{Fore.BLUE}?{Fore.RESET} 请输入命令该在哪里执行(无位置要求的也随便输个):")
        if route.startswith(("'", '"')) and route.endswith(("'", '"')):
            route = route[1:-1]

        if not route.endswith('\\'):
            route += '\\'

        if not os.path.exists(route):
            print(f"{Fore.RED}✕{Fore.RESET} 指定的目录路径不存在")
        else:
            os.chdir(route)
            break
    
    while True:
        time_counter = input("请输入每次尝试的间隔(秒)：")
       # 检测适用性
        try:
            time_counter = int(time_counter)
            if time_counter <= 1:
                print(f"{Fore.RED}✕{Fore.RESET} 间隔过短！请指定一个大于1的值！")
            else:
                print(f"{Fore.GREEN}✓{Fore.RESET} 已设置间隔时间: {time_counter}")
                break
        except ValueError as e:
            print(f"{Fore.RED}✕{Fore.RESET} 输入的值不合法，必须为一个正整数！")
    
    counter = 0

    while True:
        counter += 1
        output = run_command(user_input)
        if "Successful" in output:
            print(f"{Fore.GREEN}✓{Fore.RESET} 执行成功！！")
            notification.notify(
                title='芙芙工具箱 | 连续命令执行尝试',
                message=f'执行成功',
                timeout=10
            )
            break
        else:
            print(f"{Fore.RED}✕{Fore.RESET} 第 {Fore.BLUE}{counter}{Fore.RESET} 次尝试失败")
            print(f"原因: {Fore.RED}{output}{Fore.RESET}")
            temp = time_counter
            for i in range(time_counter, 0, -1):
                print(f"\r{i}秒后重试...", end="")
                time.sleep(1)
            print("\r重试中...")
            time_counter = temp # 还原秒数设置

    print(f"{Fore.BLUE}[info]{Fore.RESET} 一共执行了 {Fore.BLUE}{counter}{Fore.RESET} 次命令")

if __name__ == "__main__":
    main()
    input ("按Enter键退出...")
