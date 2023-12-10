import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from translate import Translator

def on_entry_click(event):
    if entry.get("1.0", "end-1c") == 'Please enter your text here...':
        entry.delete("1.0", tk.END) # 删除默认文本
        entry.config(fg = 'black') # 修改文字颜色

def translate():
    text = entry.get("1.0", "end-1c")
    translator = Translator(from_lang='en', to_lang='zh')
    translation = translator.translate(text)
    result_text.configure(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, translation)
    result_text.configure(state="disabled")

# 创建窗口
window = tk.Tk()
window.title("翻译程序")

# 设置窗口大小和位置
window.geometry('400x500+500+300')

# 创建输入框和提示信息
entry_frame = tk.Frame(window)
entry_frame.pack(pady=20)

label = tk.Label(entry_frame, text="请输入需要翻译的英文文本（500字以内）：")
label.pack(side=tk.TOP)

entry = ScrolledText(entry_frame, height=10, width=30, fg='grey')
entry.insert("1.0", 'Please enter your text here...')
entry.bind('<FocusIn>', on_entry_click) # 绑定获取焦点事件
entry.pack(fill=tk.BOTH)

# 创建翻译按钮
translate_button = tk.Button(window, text="翻译", command=translate)
translate_button.pack(pady=10)

# 创建结果文本框
result_text = ScrolledText(window, height=10, width=40, state="disabled")
result_text.pack(pady=20)

# 创建提示信息
limit_label = tk.Label(window, text="（使用时请连接网络）")
limit_label.pack()

# 运行窗口
window.mainloop()
