import requests
import time
import os

def check_wlan():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get("https://www.bilibili.com", headers=headers)
        if response.status_code == 200:
            print("Connection is successful!")
        else:
            print("Connection failed with status code:", response.status_code)
    except Exception as e:
        print("Connection failed!")
        print("Error:", e)

#---

while True:
    print("Attempting to connect...")
    print("-------------------")

    check_wlan() # checking connection

    # Wait for next check
    print("-------------------")
    for i in range(10, 0, -1):
        print("\rNext check in {}s...".format(i), end="")
        time.sleep(1)

    # Cross-platform method to clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
