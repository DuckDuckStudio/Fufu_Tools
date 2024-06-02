import tkinter as tk
from tkinter import messagebox
import sys
import random
import os

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

def generate_password():
    # 获取密码长度
    try:
        password_length = int(password_length_entry.get())
    except ValueError:
        messagebox.showerror("错误", "密码长度必须是一个整数")
        return

    # 读取config.ini文件中的character_set值
    character_set = get_character_set_from_config()
    if not character_set:
        messagebox.showerror("错误", "未找到字符集")
        return

    # 生成密码
    password = ''.join(random.choice(character_set) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    # 复制密码到剪贴板
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("提示", "密码已复制到剪贴板")

def edit_ini_file():
    # 创建自定义对话框
    dialog = tk.Toplevel(root)
    dialog.title("输入")
    dialog.geometry("300x150")

    label = tk.Label(dialog, text="请在此输入字符集:")
    label.pack(pady=10)

    entry = tk.Entry(dialog)
    entry.pack(pady=5)

    # 定义确认按钮的动作
    def confirm():
        character_set_value = entry.get()
        if character_set_value.strip() != "":
            # 转义字符%，排除;"等
            character_set_value = character_set_value.replace('%', '%%').replace(';', '').replace('"', '')
            # 修改config.ini文件
            with open('config.ini', 'r') as f:
                lines = f.readlines()
            with open('config.ini', 'w') as f:
                for line in lines:
                    if line.startswith('character_set'):
                        f.write(f'character_set={character_set_value}\n')
                    else:
                        f.write(line)
            messagebox.showinfo("提示", "INI文件已更新")
            dialog.destroy()
        else:
            messagebox.showwarning("警告", "字符集不能为空")

    # 创建确认按钮
    confirm_button = tk.Button(dialog, text="确认", command=confirm)
    confirm_button.pack(side="left", padx=10)

    # 定义取消按钮的动作
    def cancel():
        messagebox.showinfo("提示", "已取消更新INI文件")
        dialog.destroy()

    # 创建取消按钮
    cancel_button = tk.Button(dialog, text="取消", command=cancel)
    cancel_button.pack(side="right", padx=10)


def get_character_set_from_config():
    # 从config.ini文件中获取character_set的值
    character_set = None
    with open('config.ini', 'r') as f:
        for line in f:
            if line.startswith('character_set'):
                character_set = line.split('=')[1].strip()
                break
    return character_set

root = tk.Tk()
root.title("随机密码生成器")
icon_path = '..\\..\\ico.ico'  # ICO格式的图标文件路径
root.iconbitmap(icon_path)

# 居中显示窗口
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# 密码长度标签和文本框
password_length_label = tk.Label(root, text="密码长度:")
password_length_label.pack(pady=(20, 0))
password_length_entry = tk.Entry(root)
password_length_entry.pack(pady=(0, 10))

# 生成密码按钮
generate_button = tk.Button(root, text="生成密码", command=generate_password)
generate_button.pack()

# 显示密码的文本框
password_entry = tk.Entry(root)
password_entry.pack(pady=10, padx=20, fill=tk.X)

# 复制密码按钮
copy_button = tk.Button(root, text="复制密码", command=copy_to_clipboard)
copy_button.pack()

# 编辑INI文件按钮
edit_ini_button = tk.Button(root, text="修改字符集", command=edit_ini_file)
edit_ini_button.pack(side=tk.BOTTOM, pady=(0, 20), padx=20, anchor='sw')

root.mainloop()
