import os

print("感谢你使用本程序")
print("(本程序仅查找相同名称的文件，不限格式)")
file_route = input("请输入你要查找的目录: ")

if file_route.startswith(("'", '"')) and file_route.endswith(("'", '"')):
    file_route = file_route[1:-1]

if not file_route.endswith('\\'):
    file_route += '\\'

file_name = input("请输入你要查找文件的名称: ")

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 避免意外的输出位置

result_file_path = os.path.join(os.getcwd(), '查找结果.txt')
with open(result_file_path, 'w', encoding='utf-8') as result_file:
    for root, dirs, files in os.walk(file_route):
        for file in files:
            if file_name in file:
                result_file.write(os.path.join(root, file) + '\n')

print("程序运行结束，请查看程序所在目录下生成的文件！")
os.system("start " + result_file_path)
input("按Enter键继续...")
