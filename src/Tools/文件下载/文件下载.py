import os
import urllib.request

print("注意：在下载无法直接下载的文件(例如xx网盘)时可能会无法下载！")

file_route = input("请输入你需要将文件下载到哪个文件夹：")
if not file_route.endswith("\\"):
    file_route += "\\"
os.chdir(file_route)

downurl = input("请输入文件下载链接：")

filename = os.path.basename(downurl)
try:
    urllib.request.urlretrieve(downurl, filename)
    print("下载完成！")
except Exception as e:
    print("下载出现错误:", e)

input("按Enter键继续...")
