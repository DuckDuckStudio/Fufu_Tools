import os

# 输入需要藏的图片、需要藏的文件、生成的藏完文件的图片的路径和文件名
while True:
    try:
        image_path = input("请输入需要藏文件的图片路径：").strip('"')
        file_path = input("请输入需要藏的文件路径：").strip('"')
        output_path = input("请输入生成的藏完文件的图片的路径和文件名：").strip('"')
        if not os.path.isfile(image_path) or not os.path.isfile(file_path):
            raise ValueError("输入的图片路径或文件路径不存在，请重新输入！")
        break
    except ValueError as e:
        print(str(e))

# 读取需要藏的图片和文件
with open(image_path, "rb") as img_file:
    image_data = img_file.read()
with open(file_path, "rb") as file:
    file_data = file.read()

# 将文件藏在图片中
output_data = image_data + file_data

# 生成藏完文件的图片
with open(output_path, "wb") as output:
    output.write(output_data)

print ("成功将文件藏在图片中！")

input ("按任意键继续")