import requests
from bs4 import BeautifulSoup

def check_indexed_in_search_engines(url):
    search_engines = ['baidu', 'bing', 'google', 'yahoo']
    
    for search_engine in search_engines:
        if search_engine.lower() == 'baidu':
            query = f'site:{url}'
            search_url = f"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd={query}&rsv_pq=a43b358b00e3fbf6&rsv_t=3680Nponm%2FFO0m0joY50ameSwJgTz9hY2Vw9fH2SWdvoJmTTXf2egGp%2Bviw&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_btype=t"
        elif search_engine.lower() == 'bing':
            query = f'site:{url}'
            search_url = f"https://www.bing.com/search?q={query}"
        elif search_engine.lower() == 'google':
            query = f'site:{url}'
            search_url = f"https://www.google.com/search?q={query}"
        elif search_engine.lower() == 'yahoo':
            query = f'site:{url}'
            search_url = f"https://search.yahoo.com/search?p={query}"
        else:
            print('[ERROR]不支持的搜索引擎(怎么会出现这个错误，不应该啊...)')
            print('[Warn]啊，被你看到了...如果你看到了这个错误，请在下面这个链接提交Issues：')
            print('[up Issues]https://github.com/DuckDuckStudio/Fufu_Tools/issues')
            return

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            response = requests.get(search_url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            if search_engine.lower() == 'baidu':
                result_stats = soup.find(class_='nums')
            elif search_engine.lower() == 'bing':
                result_stats = soup.find('span', class_='sb_count') or soup.find('span', class_='b_algo')
            elif search_engine.lower() == 'google':
                result_stats = soup.find(id='result-stats')
            elif search_engine.lower() == 'yahoo':
                result_stats = soup.find(class_='compPagination')

            if result_stats:
                print(f'您的网站 {url} 已在 {search_engine} 中索引: {result_stats.text}')
            else:
                print(f'您的网站 {url} 未在 {search_engine} 中索引')

        except requests.RequestException as e:
            print(f'[ERROR]无法连接到 {search_engine}，请检查您的网络连接。')
        except Exception as e:
            print(f'[ERROR]检查 {search_engine} 时发生错误：{e}')

# 输入要检查的网站 URL
print("[Warn]由于技术原因，本程序不能保证结果正确。")
url = input("请输入需要检测的url：")
check_indexed_in_search_engines(url)

input("按Enter键继续...")
