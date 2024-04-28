import os
from tqdm import tqdm
from colorama import init, Fore

init(autoreset=True)  # 初始化 Colorama，使颜色输出生效

def replace_text_in_files(folder_path, old_text, new_text):
    files_processed = 0
    files_modified = 0
    matching_occurrences = 0
    errors = 0

    # 遍历文件夹中的所有文件
    for root, _, files in os.walk(folder_path):
        for file in tqdm(files, desc='Processing', unit='file', leave=False):
            file_path = os.path.join(root, file)
            try:
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 计算匹配次数
                occurrences = content.count(old_text)
                matching_occurrences += occurrences

                # 替换文本并写回文件
                content = content.replace(old_text, new_text)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

                files_processed += 1
                files_modified += 1

            except Exception as e:
                print(Fore.RED + f"\n[ERROR]无法处理文件：{file_path}\n因为： {e}")
                errors += 1
                files_processed += 1

    print(f"处理完成！共处理 {files_processed} 个文件，其中 {errors} 个文件出错，{matching_occurrences} 处匹配。")

# 设置要替换的文本和文件夹路径
folder_path = r"D:\Duckhome\CodeDebug\[测试用代码,勿删]\file"
old_text = r"yazicbs.github.io"
new_text = r"website"

# 调用函数进行文本替换
replace_text_in_files(folder_path, old_text, new_text)

input("按 ENTER 键继续...")
