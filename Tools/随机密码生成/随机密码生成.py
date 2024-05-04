import tkinter as tk
from tkinter import messagebox, simpledialog
import string
import random
import os

# 将工作目录更改为脚本所在的目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
        messagebox.showerror("错误", "未找到character_set的值")
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
    # 提示用户输入character_set的值
    character_set_value = simpledialog.askstring("输入", "请输入character_set的值:")
    if character_set_value:
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
edit_ini_button = tk.Button(root, text="配置INI", command=edit_ini_file)
edit_ini_button.pack(side=tk.BOTTOM, pady=(0, 20), padx=20, anchor='sw')

root.mainloop()
