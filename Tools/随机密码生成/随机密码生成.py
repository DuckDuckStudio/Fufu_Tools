import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation * 2
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

while True:
    try:
        length = int(input("请输入要生成的密码位数："))
        password = generate_password(length)
        print("生成的随机密码为：", password)
        break
    except ValueError:
        print("输入无效，请输入一个有效的数字作为密码位数！")

input("按Enter键继续...")
