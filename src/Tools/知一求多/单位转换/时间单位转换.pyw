from tkinter import Tk, Label, Entry, Button, StringVar, END, messagebox

# 不对 year 与 month 支持原因：
# year 与 month 具体天数不定。

# 定义计算函数
def calculate():
    input_fields = [entry_day, entry_hr, entry_min, entry_sec]
    input_values = [float(entry.get()) if entry.get() else None for entry in input_fields]

    if sum(value is not None for value in input_values) != 1:
        messagebox.showerror("错误", "请且只能输入一个参数！")
    else:
        try:
            day, hr, min, sec = input_values
            if day is not None:
                hr = 24 * day
                min = 24 * 60 * day
                sec = 24 * 60 * 60 * day
            elif hr is not None:
                day = hr / 24
                min = 60 * hr
                sec = 60 * 60 * hr
            elif min is not None:
                hr = min / 60
                day = hr / 24
                sec = 60 * min
            elif sec is not None:
                min = sec / 60
                hr = min / 60
                day = hr / 24

            result_day.set(str(day))
            result_hr.set(str(hr))
            result_min.set(str(min))
            result_sec.set(str(sec))

            for entry in input_fields:
                entry.delete(0, END)

        except ValueError:
            messagebox.showerror("错误", "请输入有效数字！")

# 创建主窗口
root = Tk()
root.title("时间单位转换器")

# 创建标签和输入框
label_day = Label(root, text="天数：")
entry_day = Entry(root)
label_hr = Label(root, text="小时：")
entry_hr = Entry(root)
label_min = Label(root, text="分钟：")
entry_min = Entry(root)
label_sec = Label(root, text="秒数：")
entry_sec = Entry(root)

# 创建结果标签
result_day = StringVar()
result_hr = StringVar()
result_min = StringVar()
result_sec = StringVar()

label_result_day = Label(root, textvariable=result_day)
label_result_hr = Label(root, textvariable=result_hr)
label_result_min = Label(root, textvariable=result_min)
label_result_sec = Label(root, textvariable=result_sec)

# 创建按钮
button_calculate = Button(root, text="计算", command=calculate)

# 添加到界面上，并使内容在程序中心显示
label_day.grid(row=0, column=0, padx=10, pady=5)
entry_day.grid(row=0, column=1, padx=10, pady=5)
label_hr.grid(row=1, column=0, padx=10, pady=5)
entry_hr.grid(row=1, column=1, padx=10, pady=5)
label_min.grid(row=2, column=0, padx=10, pady=5)
entry_min.grid(row=2, column=1, padx=10, pady=5)
label_sec.grid(row=3, column=0, padx=10, pady=5)
entry_sec.grid(row=3, column=1, padx=10, pady=5)

label_result_day.grid(row=0, column=2, padx=10, pady=5)
label_result_hr.grid(row=1, column=2, padx=10, pady=5)
label_result_min.grid(row=2, column=2, padx=10, pady=5)
label_result_sec.grid(row=3, column=2, padx=10, pady=5)

button_calculate.grid(row=4, column=1, pady=10)

# 运行主循环
root.mainloop()
