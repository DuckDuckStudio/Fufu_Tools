import os
import sys

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

print("感谢你使用本程序")
print("(本程序仅查找相同名称的文件，不限格式)")
file_route = input("请输入你要查找的目录: ")

if file_route.startswith(("'", '"')) and file_route.endswith(("'", '"')):
    file_route = file_route[1:-1]

if not file_route.endswith('\\'):
    file_route += '\\'

if not os.path.exists(file_route):
    print("指定的目录路径不存在，请重新运行程序并输入有效的目录路径。")
    input("按 ENTER 键继续...")
    exit()

file_name = input("请输入你要查找文件的名称: ")

result_file_path = os.path.join(os.getcwd(), '查找结果.txt')

def find_files_by_name(folder_path: str, file_name: str):
    files_found: list[str] = []
    total_files = sum(len(files) for _, _, files in os.walk(folder_path))
    files_processed = 0

    # 遍历文件夹中的所有文件
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file_name in file:
                files_found.append(os.path.join(root, file))

            files_processed += 1
            progress = files_processed / total_files * 100
            print(f"\r处理进度: {progress:.2f}%", end='')

    return files_found

# 调用函数查找指定名称的文件
found_files = find_files_by_name(file_route, file_name)

# 将结果写入文件
with open(result_file_path, 'w', encoding='utf-8') as result_file:
    for file_path in found_files:
        result_file.write(file_path + '\n')

print("\n程序运行结束，请查看程序所在目录下生成的文件！")
os.system("start " + result_file_path)
input("按Enter键继续...")
