from tkinter import Tk, filedialog
from PIL import Image
import piexif

# 创建GUI窗口
root = Tk()
root.withdraw()

# 显示文件选择对话框，让用户选择要转换的图片文件
file_paths = filedialog.askopenfilenames(filetypes=[('JPEG Files', '*.jpg'), ('PNG Files', '*.png'), ('BMP Files', '*.bmp'), ('HEIC Files', '*.heic')])

# 如果用户选择了文件，则进行转换
if file_paths:
    for file_path in file_paths:
        # 获取文件扩展名
        extension = file_path.split('.')[-1].lower()

        if extension == 'heic':  # 处理HEIC格式图像
            # 打开HEIC图片文件
            with open(file_path, 'rb') as f:
                heic_data = f.read()

            # 将HEIC图像数据转换为JPEG格式
            image = Image.frombytes('RGB', (512, 512), heic_data, 'raw', 'RGB', 0, 1)

            # 生成保存路径和文件名
            save_file_path = file_path[:-len(extension)] + 'jpg'
        else:  # 处理其他格式的图像
            # 打开图片文件
            image = Image.open(file_path)

            # 生成保存路径和文件名
            save_file_path = file_path

        # 设置保存文件的扩展名
        save_extension = save_file_path.split('.')[-1].lower()

        # 转换并保存为指定格式的图片文件
        if save_extension == 'jpg' or save_extension == 'jpeg':  # 要保存为JPEG格式
            if extension == 'jpg' or extension == 'jpeg' or extension == 'heic':  # 如果原文件已经是JPEG格式或HEIC格式，则直接保存
                image.save(save_file_path)
            else:  # 否则先转换为RGB模式再保存
                image = image.convert('RGB')
                image.save(save_file_path, quality=95)
        elif save_extension == 'png':  # 要保存为PNG格式
            if extension == 'png':  # 如果原文件已经是PNG格式，则直接保存
                image.save(save_file_path)
            else:  # 否则先转换为RGBA模式再保存
                image = image.convert('RGBA')
                image.save(save_file_path)
        elif save_extension == 'bmp':  # 要保存为BMP格式
            if extension == 'bmp':  # 如果原文件已经是BMP格式，则直接保存
                image.save(save_file_path)
            else:  # 否则先转换为RGB模式再保存
                image = image.convert('RGB')
                image.save(save_file_path)
        else:  # 对于其他格式，保持原样保存
            image.save(save_file_path)

        if extension != 'heic':
            # 在保存的图像中保存EXIF元数据（可选）
            exif_dict = piexif.load(file_path)
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, save_file_path)

    print('转换完成！')
else:
    print('未选择图片文件，转换取消。')
