import os
from colorama import init, Fore

init(autoreset=True) # 初始化 Colorama，使颜色输出生效
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 避免意外的输出位置

print("感谢你使用本程序")
print("(本程序仅查找含有指定文本的文件)")
folder_path = input("请输入要查找的目录路径: ")
search_text = input("请输入要查找的文本内容: ")

if folder_path.startswith(("'", '"')) and folder_path.endswith(("'", '"')):
    folder_path = folder_path[1:-1]

if not folder_path.endswith('\\'):
    folder_path += '\\'

if not os.path.exists(folder_path):
    print("指定的目录路径不存在，请重新运行程序并输入有效的目录路径。")
    input("按 ENTER 键继续...")
    exit()

result_file_path = os.path.join(os.getcwd(), '查找结果.txt')

def find_files_with_text(folder_path, search_text):
    files_found = []
    # 文件计数
    total_files = sum(len(files) for _, _, files in os.walk(folder_path))
    files_processed = 0

    # 遍历文件夹中的所有文件
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 检查文件内容是否包含指定文本
                if search_text in content:
                    files_found.append(file_path)

            except UnicodeDecodeError:
                print(f"\n{Fore.RED}[ERROR]无法处理文件：{file_path}\n因为: 文件无法通过{Fore.YELLOW}UTF-8{Fore.RED}编码读取")

            except Exception as e:
                print(Fore.RED + f"\n[ERROR]无法处理文件：{file_path}\n因为: {e}")

            files_processed += 1
            progress = files_processed / total_files * 100
            print(f"\r处理进度: {progress:.2f}%", end='')

    return files_found

# 调用函数查找含有指定文本的文件
found_files = find_files_with_text(folder_path, search_text)

# 将结果写入文件
with open(result_file_path, 'w', encoding='utf-8') as result_file:
    for file_path in found_files:
        result_file.write(file_path + '\n')

print("\n程序运行结束，请查看程序所在目录下生成的文件！")
os.system("start " + result_file_path)
input("按 ENTER 键继续...")
