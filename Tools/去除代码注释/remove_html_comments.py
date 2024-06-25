import tkinter as tk
from tkinter import filedialog
import re
import os

def remove_html_comments(content):
    # 移除HTML注释
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    return content

def remove_script_style_comments(content):
    # 移除<script>和<style>标签内的注释
    def replacer(match):
        # JavaScript或CSS内容
        text = match.group(0)
        # 移除JavaScript的单行和多行注释
        text = re.sub(r'//.*?\n', '\n', text)
        text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
        return text
    
    # 对<script>和<style>标签内的内容应用replacer函数
    content = re.sub(r'(<script[\s\S]*?>)([\s\S]*?)(</script>)', replacer, content)
    content = re.sub(r'(<style[\s\S]*?>)([\s\S]*?)(</style>)', replacer, content)
    return content

def remove_comments_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    content = remove_html_comments(content)
    content = remove_script_style_comments(content)
    
    return content

def save_new_file(original_file_path, new_content):
    base_name = os.path.basename(original_file_path)
    new_file_name = f"{os.path.splitext(base_name)[0]}-去除注释{os.path.splitext(base_name)[1]}"
    new_file_path = os.path.join(os.path.dirname(original_file_path), new_file_name)
    new_file_path = os.path.normpath(new_file_path)
    
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(new_content)
    
    print(f"处理后的文件已保存为：{new_file_path}")

def main():
    root = tk.Tk()
    root.withdraw()  # 不显示主窗口
    
    file_path = filedialog.askopenfilename(filetypes=[("HTML文件", "*.html *.htm")])
    if not file_path:
        print("没有选择文件。")
        return
    
    new_content = remove_comments_from_html(file_path)
    save_new_file(file_path, new_content)

if __name__ == "__main__":
    main()

input ("按Enter键继续...")