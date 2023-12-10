import webbrowser
import tkinter as tk
from tkinter import font, filedialog

def batch_search():
    search_content = input_text.get("1.0", tk.END).strip()
    search_urls = search_content.split('\n')
    for url in search_urls:
        if url:
            search_url = 'https://www.bing.com/search?q={}'.format(url)
            webbrowser.open(search_url)

def import_content():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            input_text.delete('1.0', tk.END)
            input_text.insert('1.0', content)

window = tk.Tk()
window.title("批量搜索")
window.geometry("300x250")

# 添加提示文本
prompt_text = "请在这里输入您需要查找的内容，每行一个..."
input_text_var = tk.StringVar()
input_text_var.set(prompt_text)

# 定义提示文本字体样式
font_style = font.Font(family="Helvetica", slant="italic", size=10)

# 创建文本框并设置提示文本样式
input_text = tk.Text(window, height=10, width=30, font=font_style)
input_text.insert('1.0', prompt_text)
input_text.bind('<FocusIn>', lambda event, arg=input_text: input_text.delete('1.0', 'end') if input_text.get('1.0', 'end-1c') == prompt_text else None)
input_text.bind('<FocusOut>', lambda event, arg=input_text: input_text.insert('1.0', prompt_text) if not input_text.get('1.0', 'end-1c') else None)
input_text.pack(side=tk.TOP, anchor=tk.CENTER)

search_button = tk.Button(window, text="搜索", command=batch_search)
search_button.pack(side=tk.TOP, anchor=tk.CENTER)

import_button = tk.Button(window, text="导入搜索内容", command=import_content)
import_button.pack(side=tk.BOTTOM, anchor=tk.SW)

# 让窗口居中
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.mainloop()
