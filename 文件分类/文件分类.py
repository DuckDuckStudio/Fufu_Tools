import os
import shutil

# 提示
print("---文件分类工具---")

# 获取文件夹路径
trash_bin_path = input('请输入文件夹路径：')

# 提示
print("---开始分类---")

# 定义文件类型及对应目录
file_types = {
    '纯文本': ['txt'],
    'Markdown': ['md'],
    'Word': ['doc', 'docx'],
    'PDF': ['pdf'],
    '代码': ['py', 'java', 'cpp', 'c', 'html', 'css', 'js'],
    '日志': ['log'],
    '图像': ['jpg', 'jpeg', 'png', 'bmp', 'gif', 'svg', 'tiff'],
    '音频': ['mp3', 'wma', 'wav', 'flac', 'aac', 'ogg'],
    '视频': ['mp4', 'avi', 'mov', 'wmv', 'rmvb', 'flv', 'mkv'],
    '压缩文件': ['zip', 'rar', '7z', 'gz', 'tar'],
    '表格': ['csv', 'xls', 'xlsx'],
    '字体': ['ttf', 'otf'],
    '演示文稿': ['key', 'odp', 'ppt', 'pptx'],
    '数据库': ['db', 'sqlite', 'mysql', 'postgresql'],
}

# 创建对应目录
for type_name in file_types:
    dir_path = os.path.join(trash_bin_path, type_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

# 遍历目录下的所有文件并分类
for root, dirs, files in os.walk(trash_bin_path):
    for file_name in files:
        # 获取文件路径、文件名和扩展名
        file_path = os.path.join(root, file_name)
        file_name_no_ext, file_ext = os.path.splitext(file_name)
        # 如果文件有扩展名，根据扩展名分类
        if file_ext:
            classified = False
            for type_name, extensions in file_types.items():
                if file_ext[1:] in extensions:
                    dest_path = os.path.join(trash_bin_path, type_name, file_name)
                    shutil.move(file_path, dest_path)
                    print(f'已将{file_name}移动到{type_name}文件夹')
                    classified = True
                    break
            # 如果没有归类到任何一个文件夹，则归类到“其他”文件夹中
            if not classified:
                dest_path = os.path.join(trash_bin_path, '其他', file_name)
                shutil.move(file_path, dest_path)
                print(f'已将{file_name}移动到其他文件夹')
        # 如果文件没有扩展名，则归类到“其他”文件夹中
        else:
            dest_path = os.path.join(trash_bin_path, '其他', file_name)
            shutil.move(file_path, dest_path)
            print(f'已将{file_name}移动到其他文件夹')

# 删除空文件夹
for root, dirs, files in os.walk(trash_bin_path, topdown=False):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        if not os.listdir(dir_path):
            os.rmdir(dir_path)

print('---分类完成！---')
