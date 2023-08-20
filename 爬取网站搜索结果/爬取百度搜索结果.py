import requests
from bs4 import BeautifulSoup

def fetch_search_results(query):
    url = f"https://www.baidu.com/s?wd={query}&ie=utf-8"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.find_all("div", class_="result")
    
    results = []
    for result in search_results:
        title = result.find("h3").get_text()
        link = result.find("a")["href"]
        results.append({"title": title, "link": link})
    
    return results

# 搜索关键词
query = input ("请输入关键词：")

# 爬取搜索结果
search_results = fetch_search_results(query)

# 打印结果
print ("\n以下是",query,"来自百度的搜索结果\n")
for result in search_results:
    print(result["title"])
    print(result["link"])
    print()
