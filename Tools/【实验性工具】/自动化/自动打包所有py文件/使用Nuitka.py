import os
import sys
import subprocess
from colorama import init, Fore
from plyer import notification
import configparser

init(autoreset=True)
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0]))) # 避免意外的位置

# Using python -m nuitka to run Nuitka
print(f"{Fore.BLUE}[!]{Fore.RESET} 将使用 {Fore.BLUE}Nuitka{Fore.RESET} 打包。")

# READ config.ini file
script_dir = os.path.dirname(os.path.realpath(__file__))
config_file_path = os.path.join(script_dir, "config.ini")
config = configparser.ConfigParser()
config.read(config_file_path)
compile = config.get('Compile', 'Compile_C')

# 计数
fail = 0 # 失败的文件个数
countd = 0 # 已删除的文件个数
acount = 0 # 总文件个数
fcount = 0 # 已打包的文件个数
pyw_acount = 0
py_acount = 0

# 文件夹路径
folder_path = input("请输入文件夹路径：")

if folder_path.startswith(("'", '"')) and folder_path.endswith(("'", '"')):
    folder_path = folder_path[1:-1]

if not folder_path.endswith('\\'):
    folder_path += '\\'

if not os.path.exists(folder_path):
    print(f"{Fore.RED}✕{Fore.RESET} 指定的目录路径不存在，请重新运行程序并输入有效的目录路径。")
    input("按 ENTER 键继续...")
    exit(1)

icon_path = input("请输入图标文件路径：")
log_path = input("请输入日志文件存放文件夹：")

if not icon_path:
    icon_path = "None"
    print(f"{Fore.YELLOW}⚠{Fore.RESET} 将执行无图标打包！")
elif icon_path.startswith(("'", '"')) and icon_path.endswith(("'", '"')):
    icon_path = icon_path[1:-1]

if not log_path:
    log_path = "None"
    print(f"{Fore.YELLOW}⚠{Fore.RESET} 将执行无日志打包！")
elif not log_path.endswith('\\'):
    log_path += '\\'

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            print(Fore.BLUE + f'找到 py 文件: {file_path}')
            py_acount = py_acount + 1
        elif file.endswith('.pyw'):
            file_path = os.path.join(root, file)
            print(Fore.BLUE + f'找到 pyw 文件: {file_path}')
            pyw_acount = pyw_acount + 1
        
acount = py_acount + pyw_acount
print(f"{Fore.GREEN}一共找到了{Fore.BLUE}{acount}{Fore.GREEN}个py/pyw文件。\n其中有{Fore.BLUE}{py_acount}{Fore.GREEN}个py文件/{Fore.BLUE}{pyw_acount}{Fore.GREEN}个pyw文件。")

# 函数：记录日志并添加分隔线
def log_message(message, log_file):
    # 日志中不应存在颜色
    message = f"{message}"
    log_file.write(message + "\n")
    log_file.write("-" * 50 + "\n") # 添加分隔线


def out_put(message, success=True):
    global fail
    # 改变控制台输出颜色
    if success:
        print(Fore.GREEN + message)
    else:
        fail = fail + 1
        notification.notify(
            title='Nuitka快速打包程序提醒您',
            message=f'打包程序炸啦！到现在一共炸了{fail}次。',
            timeout=10
        )
        print(Fore.RED + message)

# 函数：打包 Python 文件
def package_py(file_path, log_file="None"):
    global fcount
    try:
        output_dir = os.path.dirname(file_path) # 设置输出目录为 Python 文件所在目录
        if icon_path == "None":
            command = f"python -m nuitka --output-dir=\"{output_dir}\" --show-progress --onefile --remove-output --{compile} {file_path}"
        else:
            command = f"python -m nuitka --output-dir=\"{output_dir}\" --show-progress --windows-icon-from-ico=\"{icon_path}\" --onefile --remove-output --{compile} {file_path}"
        subprocess.run(command, shell=True, check=True)
        if log_file != "None":
            log_message(f"打包完成：{file_path}", log_file)
        out_put(f"打包完成：{file_path}")
        fcount += 1
        out_put(f"还剩{acount-fcount}个文件待打包。")
    except subprocess.CalledProcessError as e:
        error_message = f"打包失败：{file_path}，错误信息：{e}"
        if log_file != "None":
            log_message(error_message, log_file)
        out_put(error_message, success=False)
        fcount += 1
        out_put(f"还剩{acount-fcount}个文件待打包。")
        return file_path

# 函数：打包 Pythonw 文件
def package_pyw(file_path, log_file="None"):
    global fcount
    try:
        output_dir = os.path.dirname(file_path) # 设置输出目录为 Pythonw 文件所在目录
        if icon_path == "None":
            command = f"python -m nuitka --disable-console --plugin-enable=tk-inter --output-dir=\"{output_dir}\" --show-progress --onefile --remove-output --{compile} {file_path}"
        else:
            command = f"python -m nuitka --disable-console --plugin-enable=tk-inter --output-dir=\"{output_dir}\" --show-progress --windows-icon-from-ico=\"{icon_path}\" --onefile --remove-output --{compile} {file_path}"
        subprocess.run(command, shell=True, check=True)
        if log_file != "None":
            log_message(f"打包完成：{file_path}", log_file)
        out_put(f"打包完成：{file_path}")
        fcount += 1
        out_put(f"还剩{acount-fcount}个文件待打包。")
    except subprocess.CalledProcessError as e:
        error_message = f"打包失败：{file_path}，错误信息：{e}"
        if log_file != "None":
            log_message(error_message, log_file)
        out_put(error_message, success=False)
        fcount += 1
        out_put(f"还剩{acount-fcount}个文件待打包。")
        return file_path

# 打开日志文件，准备记录日志
if log_path == "None":
    failed_files = [] # 存储打包失败的文件名

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # 根据文件后缀选择打包方式
            if file.endswith(".py"):
                failed_file = package_py(file_path)
                if failed_file:
                    failed_files.append(failed_file)
            elif file.endswith(".pyw"):
                failed_file = package_pyw(file_path)
                if failed_file:
                    failed_files.append(failed_file)
else:
    with open(f"{log_path}packaging_log.log", "a") as log_file:
        log_message(f"开始打包，需要打包的文件数量：{acount}", log_file)

        failed_files = [] # 存储打包失败的文件名

        # 遍历文件夹中的所有文件
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # 根据文件后缀选择打包方式
                if file.endswith(".py"):
                    failed_file = package_py(file_path, log_file)
                    if failed_file:
                      failed_files.append(failed_file)
                    log_message(f"剩余待打包文件数量：{acount-fcount}", log_file)
                elif file.endswith(".pyw"):
                    failed_file = package_pyw(file_path, log_file)
                    if failed_file:
                        failed_files.append(failed_file)
                    log_message(f"剩余待打包文件数量：{acount-fcount}", log_file)

# 提示用户打包完成
if fail != 0:
    input(f"打包完成，一共炸了{fail}次。请按 Enter 键继续清除原文件...")
    notification.notify(
        title='Nuitka快速打包程序提醒您',
        message=f'打包完成，一共炸了{fail}次。',
        timeout=10
    )
    # 输出打包失败的文件
    print("以下文件打包失败：")
    for failed_file in failed_files:
        print(failed_file)
else:
    notification.notify(
        title='Nuitka快速打包程序提醒您',
        message=f'打包完成，没炸！',
        timeout=10
    )
    input(f"打包完成，没炸！请按 Enter 键继续清除原文件...")

# 删除指定格式的文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py') or file.endswith('.pyw'):
            file_path = os.path.join(root, file)
            countd = countd + 1
            os.remove(file_path)
            print(f'已删除源文件: {file_path} (还剩{acount-countd}个源文件)')

notification.notify(
    title='Nuitka快速打包程序提醒您',
    message=f'文件删除完成！总共删除了{countd}个原文件',
    timeout=10
)
print(f"文件删除完成！总共删除了{countd}个原文件")

input ("按 ENTER 键继续...")