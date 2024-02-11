import os

os.system("adb kill-server")
sleep(2)
os.system("adb start-server")

