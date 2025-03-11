# -*- coding: UTF-8 -*-
"""
PROJECT_NAME fufu
PRODUCT_NAME PyCharm
NAME 定时关机
AUTHOR Pfolg
TIME 2025/3/11 10:19
"""
import tkinter as tk
import os
from tkinter import messagebox


title="Windows定时关机"

def shutdown(t):
    # 检测值
    if not 0<=t<=1440:
        messagebox.showwarning(title,"您设置的时间超出了范围 [0,1440]，请检查后重新输入，或使用命令行！")
        return
    # 确认是否关闭设备
    iscomfirm=messagebox.askyesno(title,"您确认要在 {} 分钟后关闭您的设备吗？\n如果您已设置定时，请点击否！".format(t))
    if iscomfirm:
        # 执行命令
        os.system("shutdown /s /t {}".format(t*60))

# 取消已设置（不一定）的定时
def cancelShutdown():
    iscomfirm=messagebox.askyesno(title,"您确认要取消定时关闭设备吗？不论您是否已设置定时，都将运行解除定时关闭命令！")
    if iscomfirm:
        # 执行取消
        os.system("shutdown /a")

def window():
    # 设定窗口
    root=tk.Tk()
    root.title(title)
    root.geometry("320x180+200+200")
    root.resizable(False,False)
    # 设置变量
    this_time=tk.IntVar()
    # 设置输入框
    tk.Label(root,text="设置时间\t\t\t分钟").place(relx=.2,rely=.2)
    tk.Entry(root,width=10,textvariable=this_time).place(relx=.42,rely=.2)

    # 设置按钮+功能绑定
    tk.Button(root,text="开始",width=8,command=lambda :shutdown(this_time.get())).place(relx=.2,rely=.6)
    tk.Button(root,text="取消",width=8,command=cancelShutdown).place(relx=.6,rely=.6)

    # 添加提醒
    tk.Label(root,text="在使用之前请知悉程序的使用方法！",foreground="red").place(relx=.18,rely=.9)

    root.mainloop()
if __name__ == '__main__':
    window()