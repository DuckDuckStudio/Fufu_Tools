import os
from tqdm import tqdm

print("正在删除缓存文件...")

temp_path = os.environ["TEMP"]
username = os.environ["USERNAME"]
local_temp_path = f"C:\\Documents and Settings\\{username}\\Local Settings\\temp"
tmp_path = os.environ["TMP"]

# 获取所有缓存文件路径
file_paths = []
for root, dirs, files in os.walk(temp_path):
    for file in files:
        file_paths.append(os.path.join(root, file))
for root, dirs, files in os.walk(local_temp_path):
    for file in files:
        file_paths.append(os.path.join(root, file))
for root, dirs, files in os.walk(tmp_path):
    for file in files:
        file_paths.append(os.path.join(root, file))

total_files = len(file_paths)

# 使用tqdm显示进度条
with tqdm(total=total_files, ncols=80) as pbar:
    for file_path in file_paths:
        try:
            os.remove(file_path)
        except PermissionError:
            pass
        except OSError:
            pass
        finally:
            pbar.update(1)

print("缓存文件删除完成！按任意键退出！")
input()
