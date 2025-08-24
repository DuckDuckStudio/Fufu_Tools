import os
import sys
import time
import random
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

# 标志变量，用于检查随机过程是否正在运行
is_random_running = False

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

def load_messages(filename: str) -> list[str]:
    """从指定的文件中加载消息，忽略空行"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            messages = file.read().splitlines()
            messages = [message.strip() for message in messages if message.strip()]
            return messages
    except FileNotFoundError:
        messagebox.showerror("错误", f"文件'{filename}'未找到。")
        return []

def random_process():
    """执行随机过程"""
    global is_random_running
    global script_dir
    try:
        messages = load_messages(os.path.join(script_dir, "messages.txt"))
        if not messages:
            messagebox.showerror("错误", "内容文件为空或未找到。")
            start_button.config(state=tk.NORMAL)
            return

        result_label.config(bg='white', relief='flat', highlightthickness=0)

        for _ in range(30):
            temp_message = random.choice(messages)
            result_var.set(temp_message)
            root.update()
            time.sleep(0.1)

        final_message = random.choice(messages)
        result_var.set(final_message)
        root.update()
        time.sleep(1)

        result_label.config(
            bg='SystemButtonFace',
            relief='solid',
            bd=2,
            highlightbackground='red',
            highlightcolor='red',
            highlightthickness=2
        )
        start_button.config(state=tk.NORMAL)
    finally:
        is_random_running = False # 重置标志

def start_random():
    """开始随机过程，并在文本区域展示结果"""
    global is_random_running
    if is_random_running: # 如果随机过程正在运行，则直接返回
        return

    is_random_running = True # 设置标志为 True
    start_button.config(state=tk.DISABLED) # 禁用“开始随机”按钮

    # 启动新线程运行随机过程
    threading.Thread(target=random_process, daemon=True).start()

def edit_messages():
    """编辑消息文件"""
    global script_dir
    messages_path = os.path.join(script_dir, "messages.txt")
    try:
        os.startfile(messages_path) # 尝试打开文件
    except FileNotFoundError:
        messagebox.showerror("错误", f"文件'{messages_path}'未找到。")
    except Exception as e:
        messagebox.showerror("错误", f"无法打开文件：{e}")

def import_messages():
    """导入消息文件"""
    global script_dir
    filename = filedialog.askopenfilename(title="导入内容文件", filetypes=(("文本文件", "*.txt"), ("所有文件", "*.*")))
    if filename:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                # 检查文件内容是否为空
                if not content.strip(): # 如果文件内容为空或只有空白字符
                    messagebox.showwarning("警告", "导入的文件为空，请选择包含内容的文件。")
                    return # 终止函数执行
            
                # 如果文件不为空，则写入内容
                messages_file_path = os.path.join(script_dir, "messages.txt")
                if os.path.exists(messages_file_path):
                    confirm = messagebox.askyesno("确认", "内容文件已存在，是否覆盖？")
                    if not confirm:
                        return
                with open(messages_file_path, 'w', encoding='utf-8') as outfile:
                    outfile.write(content)
            messagebox.showinfo("成功", "内容文件已更新。")
        except Exception as e:
            messagebox.showerror("错误", f"无法导入文件：{e}")

def open_or_import():
    """弹出菜单以编辑或导入消息"""
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
edit_import_button.place(relx=0, rely=1, anchor='sw')

root.mainloop()
