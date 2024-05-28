# 标准库
import os
import shutil
import subprocess

# ---------- FOR DEV ------------
# 切记不要在开发文件夹中运行这个程序！！！
# 请先clone仓库到测试文件夹再测试！！！
# -------------------------------

# ---------- 初始初始化 -------------
dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 上级目录
venv_folder_path = os.path.join(parent_dir, '.venv') # 虚拟环境目录
# -------------------------------

# ---------- 处理掉已有的虚拟环境 ---------
if os.path.exists(venv_folder_path) and os.path.isdir(venv_folder_path):
    shutil.rmtree(venv_folder_path)
    print(f"[!] 已移除旧的虚拟环境。")
# ---------------------------------------

# --------- 弄个新的 ---------
subprocess.run(['python', '-m', 'venv', venv_folder_path], check=True)
print(f"✓ 已创建新虚拟环境(venv)。")
python_exe_path = os.path.join(venv_folder_path, 'Scripts', 'python.exe')
# ---------------------------

# --------- 安装库 ---------
subprocess.run([os.path.join(venv_folder_path, 'Scripts', 'pip.exe'), 'install', 'colorama'], check=True)
subprocess.run([os.path.join(venv_folder_path, 'Scripts', 'pip.exe'), 'install', 'requests'], check=True)
# --------- 安装库 ---------

# -------- 让每个py/pyw文件都使用虚拟环境 ----------
for root, dirs, files in os.walk(parent_dir):
    if '环境配置' in root:
        continue  # 如果遇到名为"环境配置"的目录，直接跳过

    for filename in files:
        if filename.endswith('.py') or filename.endswith('.pyw'):
            file_path = os.path.join(root, filename)
            # 读取文件内容
            with open(file_path, 'r') as f:
                content = f.readlines()
            # 在第一行插入shebang行
            content.insert(0, f'#!{python_exe_path}\n')
            # 将修改后的内容写回文件
            with open(file_path, 'w') as f:
                f.writelines(content)
            print(f"✓ 已将虚拟环境信息写入 {file_path}")
# -------------------------------------------------

subprocess.run(python_exe_path, '库文件-虚拟环境', check=True)