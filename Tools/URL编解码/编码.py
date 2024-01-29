import urllib.parse

def encode_url_params(url):
    parsed_url = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed_url.query)

    # 对参数部分进行编码
    encoded_params = {}
    for key, value in params.items():
        encoded_params[key] = [urllib.parse.quote(val) for val in value]

    # 组合编码后的 URL
    encoded_query = urllib.parse.urlencode(encoded_params, doseq=True)
    encoded_url = urllib.parse.urlunparse(parsed_url._replace(query=encoded_query))

    return encoded_url

# 测试
original_url = input ("请输入链接：")
encoded_url = encode_url_params(original_url)
print ("URL编码后的链接为: " + encoded_url)
input ("按任意键继续...")
