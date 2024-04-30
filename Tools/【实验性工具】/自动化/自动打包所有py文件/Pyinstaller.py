import os
import subprocess
from colorama import init, Fore
from plyer import notification
# 计数
fail = 0
conutf = 0
aconut = 0
# 文件夹路径
print("以下所有路径请不要带引号！")
folder_path = input("请输入文件夹路径：")
icon_path = input("请输入图标文件路径(建议使用完整路径)：")
log_path = input("请输入日志文件存放文件夹(结尾不要带\)：")

init(autoreset=True)  # 初始化 Colorama，使颜色输出生效

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py') or file.endswith('.pyw'):
            file_path = os.path.join(root, file)
            print(Fore.BLUE + f'Found file: {file_path}')
            aconut = aconut + 1
print(f"一共找到了{aconut}个py/pyw文件。")

# 函数：记录日志并添加分隔线
def log_message(message, log_file, success=True):
    if success:
        message = Fore.GREEN + f"{message}"  # 设置为绿色字体
    else:
        message = Fore.RED + f"{message}"  # 设置为红色字体
        fail = fail + 1
        notification.notify(
            title='Pyinstaller快速打包程序提醒您',
            message=f'打包程序炸啦！到现在一共炸了{fail}次。',
            timeout=10
        )
    log_file.write(message + "\n")
    log_file.write("-" * 50 + "\n")  # 添加分隔线
    print(message)

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

# 打开日志文件，准备记录日志
with open(f"{log_path}\packaging_log.log", "a") as log_file:
    log_message(f"开始打包，剩余待打包文件数量：{aconut}", log_file)

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # 根据文件后缀选择打包方式
            if file.endswith(".py"):
                package_py(file_path, log_file)
                aconut -= 1
                log_message(f"剩余待打包文件数量：{aconut}", log_file)
            elif file.endswith(".pyw"):
                package_pyw(file_path, log_file)
                aconut -= 1
                log_message(f"剩余待打包文件数量：{aconut}", log_file)

# 提示用户打包完成
if fail != 0:# or use `if fail:`
    input(f"打包完成，一共炸了{fail}次。请按 Enter 键继续清除原文件...")
    notification.notify(
        title='Pyinstaller快速打包程序提醒您',
        message=f'打包完成，一共炸了{fail}次。',
        timeout=10
    )
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