import tkinter as tk
from tkinter import filedialog
import re
import os

print("[Warn]: 对于bat文件使用GBK编码。")
print("[Warn]: 如需使用utf-8编码请使用chcp 65001.")
print("是否是使用utf-8编码？")
print("[Y]是 [N]否")
temp = input("你的回答是：")
if temp.lower() in ["y", "yes", "是"]:
    editing_code = "utf-8"
    print("[INFO]: 使用utf-8编码")
elif temp.lower() in ["n", "no", "否", "不"]:
    editing_code = "gbk"
    print("[INFO]: 使用gbk编码")
else:
    print("[ERROR]: 请勿输入其他内容")



def remove_comments(file_path):
    # 正则表达式匹配注释
    single_line_comment_pattern = re.compile(r'REM.*')
    single_line_2_comment_pattern = re.compile(r'::.*')

    with open(file_path, 'r', encoding=editing_code) as file:
        content = file.read()

        # 移除注释
        content = re.sub(single_line_2_comment_pattern, '', content)
        content = re.sub(single_line_comment_pattern, '', content)

    return content

def save_new_file(original_file_path, new_content):
    # 构造新文件名
    base_name = os.path.basename(original_file_path)
    new_file_name = f"{os.path.splitext(base_name)[0]}-无注释{os.path.splitext(base_name)[1]}"
    new_file_path = os.path.join(os.path.dirname(original_file_path), new_file_name)

    # 规范化文件路径以确保斜杠方向的一致性
    new_file_path = os.path.normpath(new_file_path)

    with open(new_file_path, 'w', encoding=editing_code) as new_file:
        new_file.write(new_content)

    print(f"处理后的文件已保存为：{new_file_path}")

def main():
    root = tk.Tk()
    root.withdraw()  # 不显示主窗口

    file_path = filedialog.askopenfilename(filetypes=[
        ("批处理文件", "*.bat", "*.cmd"),
        ("所有文件", "*.*")
    ])
    if not file_path:
        print("没有选择文件。")
        return

    new_content = remove_comments(file_path)
    save_new_file(file_path, new_content)

if __name__ == "__main__":
    main()

input ("按Enter键继续...")