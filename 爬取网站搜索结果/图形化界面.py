import requests
from bs4 import BeautifulSoup
import tkinter as tk
import webbrowser

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

# ��������
window = tk.Tk()

# ���ô��ڱ���
window.title("��������")

# �����ؼ��������
query_label = tk.Label(window, text="������ؼ��ʣ�")
query_label.pack()
query_entry = tk.Entry(window)
query_entry.pack()

# ������������
def search():
    # ��ȡ�ؼ���
    query = query_entry.get()

    # ��ȡ�������
    search_results = fetch_search_results(query)

    # ������������
    result_text.delete(1.0, tk.END)

    # ��ʾ�������
    result_text.insert(tk.END, f"\n������ {query} ���԰ٶȵ��������\n���Ը������ӵ���������ʽ��\n\n")
    for i, result in enumerate(search_results):
        title = result["title"]
        link = result["link"]
        result_text.insert(tk.END, f"{i+1}. {title}\n{link}\n\n")

    # ��չؼ��������
    query_entry.delete(0, tk.END)

# ����������ť
search_button = tk.Button(window, text="����", command=search)
search_button.pack()

# �������������ʾ��
result_text = tk.Text(window)
result_text.pack()

# �������ӵ���¼�
def open_link(event):
    widget = event.widget
    idx = widget.get("current linestart", "current lineend").split(".")[0]
    if idx.isdigit():
        idx = int(idx)
        if 1 <= idx <= len(search_results):
            link = search_results[idx-1]["link"]
            webbrowser.open(link)

# �����ӵ���¼�
result_text.tag_bind("hyperlink", "<Button-1>", open_link)

# �����ı��е�������ʽ
result_text.tag_configure("hyperlink", foreground="blue", underline=True)

# ����س��������¼�
def enter_pressed(event):
    search()

window.bind("<Return>", enter_pressed)

# ���д�����ѭ��
window.mainloop()
