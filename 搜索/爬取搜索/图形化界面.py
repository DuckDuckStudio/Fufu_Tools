import requests
from bs4 import BeautifulSoup
import tkinter as tk
import webbrowser
from urllib.parse import quote

def fetch_search_results(query):
    query = quote(query)  # 对查询关键词进行URL编码
    url = f"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd={query}&rsv_pq=a43b358b00e3fbf6&rsv_t=3680Nponm%2FFO0m0joY50ameSwJgTz9hY2Vw9fH2SWdvoJmTTXf2egGp%2Bviw&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_btype=t"
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

# 创建窗口
window = tk.Tk()

# 设置窗口标题
window.title("搜索引擎")

# 创建关键词输入框
query_label = tk.Label(window, text="请输入关键词：")
query_label.pack()
query_entry = tk.Entry(window)
query_entry.pack()

# 定义搜索函数
def search():
    # 获取关键词
    query = query_entry.get()

    # 爬取搜索结果
    search_results = fetch_search_results(query)

    # 清空搜索结果框
    result_text.delete(1.0, tk.END)

    # 显示搜索结果
    result_text.insert(tk.END, f"\n以下是 {query} 来自百度的搜索结果\n可以复制链接到浏览器访问结果\n\n")
    for i, result in enumerate(search_results):
        title = result["title"]
        link = result["link"]
        result_text.insert(tk.END, f"{i+1}. {title}\n{link}\n\n")

    # 清空关键词输入框
    query_entry.delete(0, tk.END)

# 创建搜索按钮
search_button = tk.Button(window, text="搜索", command=search)
search_button.pack()

# 创建搜索结果显示框
result_text = tk.Text(window)
result_text.pack()

# 定义链接点击事件
def open_link(event):
    widget = event.widget
    idx = widget.get("current linestart", "current lineend").split(".")[0]
    if idx.isdigit():
        idx = int(idx)
        if 1 <= idx <= len(search_results):
            link = search_results[idx-1]["link"]
            webbrowser.open(link)

# 绑定链接点击事件
result_text.tag_bind("hyperlink", "<Button-1>", open_link)

# 定义文本中的链接样式
result_text.tag_configure("hyperlink", foreground="blue", underline=True)

# 定义回车键搜索事件
def enter_pressed(event):
    search()

window.bind("<Return>", enter_pressed)

# 运行窗口主循环
window.mainloop()
