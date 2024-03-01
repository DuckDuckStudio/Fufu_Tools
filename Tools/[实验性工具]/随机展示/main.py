import tkinter as tk
from tkinter import filedialog, messagebox
import random
import time
import os

def load_messages(filename):
    """从指定的文件中加载消息"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: 文件'{filename}'未找到。")
        return []

def start_random():
    """开始随机过程，并在文本区域展示结果"""
    messages = load_messages("./messages.txt")
    if not messages:
        result_var.set("错误: 内容文件为空或未找到。")
        return
    
    # 在开始新一轮随机之前，重置标签样式，移除红色边框
    result_label.config(bg='SystemButtonFace', relief='flat', highlightthickness=0)
    
    # 模拟抽奖机效果
    for _ in range(30):
        temp_message = random.choice(messages)
        result_var.set(temp_message)
        root.update()
        time.sleep(0.1)

    # 最终结果
    final_message = random.choice(messages)
    result_var.set(final_message)
    root.update()
    time.sleep(1)

    # 将最终结果用红色方框框起来
    result_label.config(bg='SystemButtonFace', relief='solid', bd=2, highlightbackground='red', highlightcolor='red', highlightthickness=2)

def open_or_import():
    """提供编辑或导入内容文件的选项"""
    def edit_messages():
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在目录的绝对路径
        messages_path = os.path.join(script_dir, "messages.txt")  # 构建messages.txt的绝对路径
        try:
            os.startfile(messages_path)  # 尝试打开文件
        except FileNotFoundError:
            messagebox.showerror("错误", f"文件'{messages_path}'未找到。")
        except Exception as e:
            messagebox.showerror("错误", f"无法打开文件：{e}")


    def import_messages():
        filename = filedialog.askopenfilename(title="导入内容文件", filetypes=(("文本文件", "*.txt"), ("所有文件", "*.*")))
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    with open("./messages.txt", 'w', encoding='utf-8') as outfile:
                        outfile.write(file.read())
                messagebox.showinfo("成功", "内容文件已更新。")
            except Exception as e:
                messagebox.showerror("错误", f"无法导入文件：{e}")

    # 创建弹出菜单
    popup = tk.Menu(root, tearoff=0)
    popup.add_command(label="编辑消息", command=edit_messages)
    popup.add_command(label="导入消息", command=import_messages)

    # 弹出菜单
    try:
        popup.tk_popup(root.winfo_rootx(), root.winfo_rooty(), 0)
    finally:
        popup.grab_release()

# 创建窗口
root = tk.Tk()
root.title("随机内容展示")
root.geometry('400x200')

# 创建结果展示变量
result_var = tk.StringVar()

# 创建标签用于展示随机结果
result_label = tk.Label(root, textvariable=result_var, font=('Arial', 12), wraplength=350, justify='left')
result_label.pack(pady=(20, 10), padx=(20, 20), expand=True, fill=tk.BOTH)

# 创建“开始随机”按钮
start_button = tk.Button(root, text="开始随机", command=start_random)
start_button.pack(pady=(0, 20), padx=(20, 20))

# 创建“编辑/导入消息”按钮
edit_import_button = tk.Button(root, text="编辑/导入消息", command=open_or_import)
edit_import_button.place(relx=0.0, rely=1.0, anchor='sw')

root.mainloop()
