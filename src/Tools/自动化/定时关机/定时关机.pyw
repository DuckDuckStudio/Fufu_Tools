# -*- coding: UTF-8 -*-
"""
PROJECT_NAME fufu
PRODUCT_NAME PyCharm
NAME 定时关机
AUTHOR Pfolg
TIME 2025/3/11 10:19
"""
import tkinter as tk
from tkinter import messagebox
import subprocess

def shutdown(t):
    # 检测值
    if t < 0:
        messagebox.showerror("错误", "你不可以输入一个负数")
        return
    # 确认是否关闭设备
    if t == 0:
        message = "您要立即关闭您的设备吗？"
    else:
        message = f"您确定要在 {t} 分钟后关闭您的设备吗？"
    if messagebox.askyesno("确认", message):
        # 执行命令
        try:
            subprocess.run(["shutdown","/s","/t",str(t*60)],check=True)
        except subprocess.CalledProcessError as event:
            # 检测是否已设置定时
            if event.returncode == 1190:
                messagebox.showerror("错误","您已设置定时，请先取消当前定时再设置！")
            else:
                messagebox.showerror("错误",f"未知的错误: {event.returncode}")

# 取消已设置的定时
def cancelShutdown():
    # 确认取消
    if messagebox.askyesno("确认","您确认要取消定时关闭设备吗？"):
        # 执行取消
        try:
            subprocess.run(["shutdown","/a"],check=True)
        except subprocess.CalledProcessError as event:
            if event.returncode==1116:
                messagebox.showinfo("信息","您尚未设置定时，没有可取消的定时！")
            else:
                messagebox.showerror("错误", "未知的错误，请反馈！")

def main():
    # 设定窗口
    root=tk.Tk()
    root.title("Windows定时关机")
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

    root.mainloop()
if __name__ == '__main__':
    main()
