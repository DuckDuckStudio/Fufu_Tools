import os
import time
import subprocess

# Warn:这个程序暂未进行过任何测试，其稳定性不可保证！

'''
1. 获取工作目录
2. 检测是否与远程仓库有差异
3. 如果是，执行3.1.1；否则执行3.2.1
3.1.1 尝试pull到本地仓库
3.1.2 如果成功，显示提醒；如果失败，执行3.1.3
3.1.3 计数+1，等待10秒后重新执行3.1.1
3.2.1 (已是最新)给与提示
'''

def process_file_path(file_path):# 处理工作目录路径
    file_path = file_path.replace('"', '').replace("'", '')
    
    if not file_path.endswith('\\'):
        file_path += '\\'
    
    return file_path

def has_unpulled_commits(working_dir):  
    result = subprocess.run('git cherry -v', shell=True, capture_output=True, text=True, cwd=working_dir)
    
    while True:
        if result.returncode == 0 and result.stdout is not None: # 检查命令是否成功执行并且有输出
            output = result.stdout.strip()
            print("[info]检测到差异：", output)
            return True
        else:
            print("[ERROR] 获取差异时出错")


def pull_commits(working_dir):  # pull提交
    result = subprocess.run('git pull', shell=True, capture_output=True, text=True, cwd=working_dir)
    if result.returncode == 0:
        return "pull successful"
    else:
        return result.stderr

def main():
    working_dir = input("请输入工作目录(绝对路径)：")
    working_dir = process_file_path(working_dir)
    print(f"[info]当前工作目录: {working_dir}")
    
    while True:
        time_counter = int(input("请输入每次尝试的间隔(秒)："))
        # 检测适用性
        if time_counter <= 1:
            print("[ERROR]间隔过短！请指定一个大于1的值！")
        else:
            break
    
    counter = 0

    while True:
        if has_unpulled_commits(working_dir):
            counter += 1
            pull_output = pull_commits(working_dir)
            if "pull successful" in pull_output:
                print("[info]pull成功")
                break
            else:
                print("[Warn]第",counter,"次pull尝试失败")
                print("原因:",pull_output)
                temp = time_counter
                for i in range(time_counter, 0, -1):
                    print("\r{}秒后重试...".format(i), end="")
                    time.sleep(1)
                print("\r")
                time_counter = temp# 还原秒数设置
        else:
            print("[Warn]本地仓库已是最新")
    print("[info]一共执行了",counter,"次pull")

if __name__ == "__main__":
    main()
    input ("按Enter键退出...")
