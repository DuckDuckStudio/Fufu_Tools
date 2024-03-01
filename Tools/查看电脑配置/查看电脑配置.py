import os

print("您的设备信息如下：")
# 执行 systeminfo 命令并输出结果
os.system("systeminfo")

# --检查--
print("是否查看更详细的信息？")
while True:
    print("[Y]是 [N]否")
    temp = input("你的回答是：")
    
    if temp.lower() in ["y", "yes", "是"]:
        print("启动页面中...")
        os.system("msinfo32")
        print("已展示，请查看弹出的窗口")
        break
    elif temp.lower() in ["n", "no", "否", "不"]:
        print("取消操作...")
        break
    else:
        you = 0
        do = 0
        what = 0
        print("请按说明回答！")

input("按Enter键继续...")