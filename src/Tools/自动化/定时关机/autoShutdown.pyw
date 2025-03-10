# -*- coding: UTF-8 -*-
"""
@Project ：Python_projects 
@File    ：autoShutdown
@IDE     ：PyCharm 
@Author  ：pfolg
@Date    ：2/6/25 2:19 PM 
"""
import os
import tkinter as tk
from tkinter import ttk,messagebox
import time
import threading

command="shutdown /s /t "
    # "Linux":"poweroff",
    # "MacOs":"shutdown -h now"



class A:
    def __init__(self,name):
        # 赋值
        self.root=tk.Tk()
        self.name=name
        self.system=tk.BooleanVar()
        self.frame=ttk.Frame(self.root)
        self.countdown=None

        # 倒计时是否已开始
        self.isstart=False
        # 时间
        self.day,self.hour,self.min,self.sec=tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()

        # 用于设定的函数
        self.set_win()
        self.set_frame()

        # 运行
        self.root.mainloop()

    # root设定函数
    def set_win(self):
        self.root.title(self.name)
        sw,sh=self.root.winfo_screenwidth(),self.root.winfo_screenheight()
        self.root.geometry("{}x{}+{}+{}".format(int(sw/4),int(sh/4),int(sw/4),int(sh/4)))
        self.root.resizable(False,False)
        # self.root.config(background="white")



    def set_frame(self,):
        # systems=list(commands.keys())
        self.system.set(False)

        # ttk.Label(self.frame,text="Windows").place(relx=0,rely=0)
        # ttk.Combobox(self.frame,values=systems,textvariable=self.system,width=10,state="readonly").place(relx=.25,rely=.05)
        ttk.Checkbutton(self.frame,text="使用系统自带功能",variable=self.system).place(relx=.1,rely=.05)

        # 定义标签
        x ,y= .1,.2
        ttk.Label(self.frame,text="天",).place(relx=x,rely=y)
        ttk.Entry(self.frame,textvariable=self.day,width=8,).place(relx=x+.2,rely=y)
        ttk.Label(self.frame, text="小时", ).place(relx=x, rely=y+.15)
        ttk.Entry(self.frame, textvariable=self.hour, width=8, ).place(relx=x + .2, rely=y+.15)
        ttk.Label(self.frame, text="分钟", ).place(relx=x, rely=y+.3)
        ttk.Entry(self.frame, textvariable=self.min, width=8, ).place(relx=x + .2, rely=y+.3)
        ttk.Label(self.frame, text="秒", ).place(relx=x, rely=y+.45)
        ttk.Entry(self.frame, textvariable=self.sec, width=8, ).place(relx=x + .2, rely=y+.45)

        # 定义按钮
        ttk.Button(self.frame,text="开始",command=lambda :threading.Thread(target=self.shutdown,daemon=True).start()).place(relx=.6,rely=.4)
        ttk.Button(self.frame,text="取消",command=self.cancel).place(relx=.6,rely=.6)

        # 倒计时label
        self.countdown=tk.Label(self.frame,text="NA",font=("微软雅黑",16))
        self.countdown.place(relx=.6,rely=.1)

        # 挂载容器/框架
        self.frame.place(x=0,y=0,height=240,width=380)


    def shutdown(self):
        # 计算总秒数
        total = ((self.day.get() * 24 + self.hour.get() )* 60  + self.min.get() )* 60 + self.sec.get()
        isconfirm=messagebox.askyesno("Confirm","Do you want to shutdown your system in {} second(s)\n您的系统将在{}秒后关闭！".format(total,total))
        if not isconfirm:
            return
        if self.system.get():
            os.system(command+str(total))
        else:
            self.isstart=True
            for i in range(total):
                # 记录开始时间
                start_time = time.time()
                if not self.isstart:
                    return
                self.countdown.config(text="{:.4f}%\n{}/{}".format(i/total*100,i,total))
                print("{:.4f}%\t{}/{}".format(i/total*100,i,total),self.isstart)
                # 记录结束时间
                end_time = time.time()
                # 计算执行时间
                execution_time = end_time - start_time
                print(f"Execution time: {execution_time:.6f} seconds")
                # 修正误差
                time.sleep(1-execution_time)
            # 执行关机
            os.system(command+"0")


    def cancel(self):
        self.isstart=False
        self.countdown.config(text="NA")
        os.system("shutdown /a")
        print("Canceled")



if __name__ == '__main__':
    A("Windows定时关机")