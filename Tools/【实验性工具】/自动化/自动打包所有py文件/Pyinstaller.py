import os
import subprocess
from colorama import init, Fore
from plyer import notification

# 计数
fail = 0
conutf = 0
aconut = 0
pyw_aconut = 0
py_acount = 0

# 文件夹路径
folder_path = input("请输入文件夹路径：")
icon_path = input("请输入图标文件路径：")
log_path = input("请输入日志文件存放文件夹：")

if icon_path.startswith(("'", '"')) and icon_path.endswith(("'", '"')):
    icon_path = icon_path[1:-1]

if not log_path.endswith('\\'):
    log_path += '\\'

init(autoreset=True)  # 初始化 Colorama，使颜色输出生效

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            print(Fore.BLUE + f'Found py file: {file_path}')
            py_acount = py_acount + 1
        elif file.endswith('.pyw'):
            file_path = os.path.join(root, file)
            print(Fore.BLUE + f'Found pyw file: {file_path}')
            pyw_aconut = pyw_aconut + 1
        
aconut = py_acount + pyw_aconut
print(f"一共找到了{aconut}个py/pyw文件。\n其中有{py_acount}个py文件/{pyw_aconut}个pyw文件。")

# 函数：记录日志并添加分隔线
def log_message(message, log_file, success=True):
    # 日志中不应存在颜色
    if success:
        message = f"{message}"
    else:
        message = f"{message}"
        fail = fail + 1
        notification.notify(
            title='Pyinstaller快速打包程序提醒您',
            message=f'打包程序炸啦！到现在一共炸了{fail}次。',
            timeout=10
        )
    log_file.write(message + "\n")
    log_file.write("-" * 50 + "\n")  # 添加分隔线
    # 改变控制台输出颜色
    if success:
        print(Fore.GREEN + message)
    else:
        print(Fore.RED + message)

# 函数：打包 Python 文件
def package_py(file_path, log_file):
    try:
        output_dir = os.path.dirname(file_path)  # 设置输出目录为 Python 文件所在目录
        command = f"pyinstaller --onefile -i \"{icon_path}\" --distpath={output_dir} {file_path}"
        subprocess.run(command, shell=True, check=True)
        log_message(f"打包完成：{file_path}", log_file)
    except subprocess.CalledProcessError as e:
        error_message = f"打包失败：{file_path}，错误信息：{e}"
        log_message(error_message, log_file, success=False)
        return file_path

# 函数：打包 Pythonw 文件
def package_pyw(file_path, log_file):
    try:
        output_dir = os.path.dirname(file_path)  # 设置输出目录为 Pythonw 文件所在目录
        command = f"pyinstaller --noconsole --onefile -i \"{icon_path}\" --distpath={output_dir} {file_path}"
        subprocess.run(command, shell=True, check=True)
        log_message(f"打包完成：{file_path}", log_file)
    except subprocess.CalledProcessError as e:
        error_message = f"打包失败：{file_path}，错误信息：{e}"
        log_message(error_message, log_file, success=False)
        return file_path

# 打开日志文件，准备记录日志
with open(f"{log_path}packaging_log.log", "a") as log_file:
    log_message(f"开始打包，剩余待打包文件数量：{aconut}", log_file)

    failed_files = []  # 存储打包失败的文件名

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # 根据文件后缀选择打包方式
            if file.endswith(".py"):
                failed_file = package_py(file_path, log_file)
                if failed_file:
                    failed_files.append(failed_file)
                aconut -= 1
                log_message(f"剩余待打包文件数量：{aconut}", log_file)
            elif file.endswith(".pyw"):
                failed_file = package_pyw(file_path, log_file)
                if failed_file:
                    failed_files.append(failed_file)
                aconut -= 1
                log_message(f"剩余待打包文件数量：{aconut}", log_file)

# 提示用户打包完成
if fail != 0:
    input(f"打包完成，一共炸了{fail}次。请按 Enter 键继续清除原文件...")
    notification.notify(
        title='Pyinstaller快速打包程序提醒您',
        message=f'打包完成，一共炸了{fail}次。',
        timeout=10
    )
    # 输出打包失败的文件
    print("以下文件打包失败：")
    for failed_file in failed_files:
        print(failed_file)
else:
    input(f"打包完成，没炸！请按 Enter 键继续清除原文件...")
    notification.notify(
        title='Pyinstaller快速打包程序提醒您',
        message=f'打包完成，没炸！',
        timeout=10
    )

# 删除指定格式的文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py') or file.endswith('.pyw'):
            file_path = os.path.join(root, file)
            print(f'Deleting file: {file_path}')
            conutf = conutf + 1
            os.remove(file_path)

print(f"文件删除完成！总共删除了{conutf}个原文件")
notification.notify(
    title='Pyinstaller快速打包程序提醒您',
    message=f'文件删除完成！总共删除了{conutf}个原文件',
    timeout=10
)

input ("按 ENTER 键继续...")