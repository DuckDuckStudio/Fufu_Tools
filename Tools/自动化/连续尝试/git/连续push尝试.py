import time
import subprocess
import tkinter as tk
from plyer import notification
from tkinter import filedialog
from colorama import init, Fore

# --- init ---
init(autoreset=True)
root = tk.Tk()
root.withdraw()
# ------------

def push_commits(working_dir): # push提交
    result = subprocess.run('git push', shell=True, capture_output=True, text=True, cwd=working_dir)
    if result.returncode == 0:
        return "push successful"
    else:
        return result.stderr

def is_network_error(stderr): # 判断错误类型
    network_error_keywords = [
        "unable to access",
        "Could not resolve host",
        "Failed to connect",
        "Operation timed out",
        "early EOF",
        "RPC failed"
    ]
    for keyword in network_error_keywords:
        if keyword in stderr:
            return True
    return False

def main():
    print(f"{Fore.BLUE}?{Fore.RESET} 请选择仓库目录", end="")
    working_dir = filedialog.askdirectory()
    print(f"\r{Fore.GREEN}✓{Fore.RESET} 选择的仓库目录: {working_dir}")
    
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
        push_output = push_commits(working_dir)
        if "push successful" in push_output:
            print(f"{Fore.GREEN}✓{Fore.RESET} 推送成功！！")
            notification.notify(
                title='芙芙工具箱 | 连续推送尝试',
                message=f'推送成功！',
                timeout=10
            )
            break
        elif is_network_error(push_output):
            print(f"{Fore.YELLOW}⚠{Fore.RESET} 第 {Fore.BLUE}{counter}{Fore.RESET} 次推送尝试失败")
            print(f"原因: {Fore.RED}{push_output}{Fore.RESET}")
            temp = time_counter
            for i in range(time_counter, 0, -1):
                print(f"\r{i}秒后重试...", end="")
                time.sleep(1)
            print("\r重试中...")
            time_counter = temp # 还原秒数设置
        else:
            print(f"{Fore.RED}✕{Fore.RESET} 第 {Fore.BLUE}{counter}{Fore.RESET} 次推送尝试失败，出现了非已知网路问题\n{Fore.BLUE}[提示]{Fore.RESET} 如果你确定这是网络问题，请提交issue或者PR，感谢！")
            print(f"原因: {Fore.RED}{push_output}{Fore.RESET}")
            notification.notify(
                title='芙芙工具箱 | 连续推送尝试',
                message=f'检测到非网络错误，请注意！',
                timeout=10
            )
            t = input("请确认是否继续尝试: ")
            if t.lower() not in ["y", "yes", "是", "继续", "确认"]:
                print(f"{Fore.RED}✕{Fore.RESET} 由于检测到非网络错误，已终止程序")
                break
    print(f"{Fore.BLUE}[info]{Fore.RESET} 一共执行了 {Fore.BLUE}{counter}{Fore.RESET} 次push")

if __name__ == "__main__":
    main()
    input ("按Enter键退出...")
