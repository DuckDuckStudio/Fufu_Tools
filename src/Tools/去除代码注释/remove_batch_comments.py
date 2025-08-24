import tkinter as tk
from tkinter import filedialog
import re
import os

def remove_comments(file_path: str):
    # 正则表达式匹配注释
    single_line_comment_pattern = re.compile(r'REM.*')
    single_line_2_comment_pattern = re.compile(r'::.*')

    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

        # 移除注释
        content = re.sub(single_line_2_comment_pattern, '', content)
        content = re.sub(single_line_comment_pattern, '', content)

    return content

def save_new_file(original_file_path: str, new_content: str):
    # 构造新文件名
    base_name = os.path.basename(original_file_path)
    new_file_name = f"{os.path.splitext(base_name)[0]}-无注释{os.path.splitext(base_name)[1]}"
    new_file_path = os.path.join(os.path.dirname(original_file_path), new_file_name)

    # 规范化文件路径以确保斜杠方向的一致性
    new_file_path = os.path.normpath(new_file_path)

    with open(new_file_path, 'w', encoding="utf-8") as new_file:
        new_file.write(new_content)

    print(f"处理后的文件已保存为：{new_file_path}")

def main():
    root = tk.Tk()
    root.withdraw() # 不显示主窗口

    file_path = filedialog.askopenfilename(filetypes=[
        ("批处理文件", ("*.bat", "*.cmd")),
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