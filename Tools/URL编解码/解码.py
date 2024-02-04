import urllib.parse

# 需要解码的 URL
url = input ("请输入链接：")

# 解码 URL
decoded_url = urllib.parse.unquote(url)

# 输出解码后的 URL
print("解码后的URL: " + decoded_url)

input ("按Enter键继续...")