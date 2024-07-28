from PIL import Image, ImageDraw, ImageFont
import os

# 获取用户输入的水印文字和图片文件夹路径
watermark_text = input("请输入水印文字：")
while True:
    image_folder = input("请输入图片文件夹路径：")
    
    if not image_folder:
        print("[Warn]请输入图片文件夹路径")
    elif os.path.exists(image_folder.strip('\"')):
        break
    else:
        print("[Warn]无效路径")

#----

while True:
    text_ttf = input("请输入自定义字体文件完整路径(默认Arial.ttf)：")

   # 如果用户没有输入任何内容或者输入了"默认"，则将变量值设为 "Arial.ttf"
    if not text_ttf or text_ttf == "默认" or text_ttf == "Arial.ttf":
        text_ttf = "Arial.ttf"
        break
    else:
       # 自动处理引号
        text_ttf = text_ttf.strip('\"')
        if os.path.exists(text_ttf):
            break
       # 检查文件路径是否存在
        else:
            print("[Warn]自定义字体文件不存在")

# 计算水印文字的宽度
text_width = len(watermark_text) * 25

print("请输入水印位置：")
print("[UL]左上 [UR]右上 [DL]左下 [DR]右下(默认)")
text_where = input("你的选择是：")
if text_where.lower() in ["ul", "左上"]:
    text_where = "[UL]左上"
elif text_where.lower() in ["ur", "右上"]:
    text_where = "[UR]右上"
elif text_where.lower() in ["dl", "左下"]:
    text_where = "[DL]左下"
else:
    text_where = "[DR]右下(默认)"

# 计算差值
move_text = len(watermark_text) * 23

print("[INFO]水印配置：\n----------\n水印文字：",watermark_text,"\n图片文件夹路径：",image_folder,"\n自定义字体：",text_ttf,"\n水印位置：",text_where,"\n----------")


# 定义添加水印的函数
def add_watermark(image_path, watermark_text, text_where, move_text):
    try:
        image = Image.open(image_path).convert("RGBA")

       # 创建水印图片
        watermark = Image.new("RGBA", image.size, (0, 0, 0, 0))
        font = ImageFont.truetype("D:\\Duckhome\\projects\\MSVS\\Source\\Repos\\windows-widgets\\Tools\\[实验性工具]\\图片处理\\O神启动.ttf", 40) # 使用默认字体和大小
        draw = ImageDraw.Draw(watermark)

       # 计算水印文本的位置
        if image.width > image.height: # 图片宽大于高，16:9
           # where
            if text_where == "[DR]右下(默认)":
                text_position = (image.width - text_width - move_text, image.height - 50)
            elif text_where == "[DL]左下":
                text_position = (text_width - move_text, image.height - 50)
            elif text_where == "[UR]右上":
                text_position = (image.width - text_width - move_text, 50)
            elif text_where == "[UL]左上":
                text_position = (text_width - move_text, 5)
           #-----
            draw.text(text_position, watermark_text, font=font, fill=(255, 255, 255, 128))
           # 添加水印
            watermarked_image = Image.alpha_composite(image, watermark)

           # 保存水印图片
            save_path = os.path.splitext(image_path)[0] + "_watermarked.png"
            watermarked_image.save(save_path)
           # only test on 4032*2268
            if image.width != 4032 or image.height != 2268:
                print("[Warn] 本工具仅在4032*2268的图片上测试过，其他图片效果可能不理想。\n本张图片大小：",image.width,"*",image.height)
            print(f"[INFO] 水印已成功添加到 {save_path}\n")
        else: # 其他
            print ("[Warn] 仅支持16:9的图片。错误文件", image_path, "\n")

    except Exception as e:
        print(f"[ERROR] 添加水印时出现错误: {e}")

# 批量添加水印
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(image_folder, filename)
        add_watermark(image_path, watermark_text, text_where, move_text)

input("[End]水印添加完毕，按Enter键退出...")