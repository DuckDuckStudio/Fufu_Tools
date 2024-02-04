import tkinter as tk
from tkinter import filedialog
import re

def remove_comments(file_path):
    # 正则表达式匹配多行注释和单行注释
    multi_line_comment_pattern = re.compile(r"('''[\s\S]*?''')")
    single_line_comment_pattern = re.compile(r"#.*")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # 移除多行注释
        content = re.sub(multi_line_comment_pattern, '', content)
        # 移除单行注释
        content = re.sub(single_line_comment_pattern, '', content)
        
    return content

def save_new_file(original_file_path, new_content):
    import os
    # 构造新文件名
    base_name = os.path.basename(original_file_path)
    new_file_name = os.path.splitext(base_name)[0] + "-去除注释.py"
    new_file_path = os.path.join(os.path.dirname(original_file_path), new_file_name)
    
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(new_content)
    
    print(f"处理后的文件已保存为：{new_file_path}")

def main():
    root = tk.Tk()
    root.withdraw()  # 不显示主窗口
    
    # 弹出文件选择对话框让用户选择文件
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py *.pyw")])
    if not file_path:
        print("没有选择文件。")
        return
    
    new_content = remove_comments(file_path)
    save_new_file(file_path, new_content)

if __name__ == "__main__":
    main()
