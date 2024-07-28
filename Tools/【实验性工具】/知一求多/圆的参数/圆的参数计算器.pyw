from tkinter import *
from tkinter import messagebox

# 定义计算函数
def calculate():
    pi_value = float(entry_pi.get())
    input_fields = [entry_r, entry_d, entry_c, entry_s]
    input_values = [float(entry.get()) if entry.get() else None for entry in input_fields]

    if sum(value is not None for value in input_values) != 1:
        messagebox.showerror("错误", "请且只能输入一个参数！")
    else:
        try:
            r, d, c, s = input_values
            if r is not None:
                d = 2 * r
                c = 2 * pi_value * r
                s = pi_value * r ** 2
            elif d is not None:
                r = d / 2
                c = pi_value * d
                s = pi_value * (d / 2) ** 2
            elif c is not None:
                r = c / (2 * pi_value)
                d = 2 * r
                s = pi_value * r ** 2
            elif s is not None:
                r = (s / pi_value) ** 0.5
                d = 2 * r
                c = 2 * pi_value * r

            result_r.set(r)
            result_d.set(d)
            result_c.set(c)
            result_s.set(s)

            for entry in input_fields:
                entry.delete(0, END)

        except ValueError:
            messagebox.showerror("错误", "请输入有效数字！")

# 创建主窗口
root = Tk()
root.title("圆的参数计算器")

# 创建标签和输入框
label_r = Label(root, text="半径r：")
entry_r = Entry(root)
label_d = Label(root, text="直径d：")
entry_d = Entry(root)
label_c = Label(root, text="周长C：")
entry_c = Entry(root)
label_s = Label(root, text="面积S：")
entry_s = Entry(root)
label_pi = Label(root, text="π的取值：")
entry_pi = Entry(root)
entry_pi.insert(0, "3.14") # 默认值为3.14

# 创建结果标签
result_r = StringVar()
result_d = StringVar()
result_c = StringVar()
result_s = StringVar()

label_result_r = Label(root, textvariable=result_r)
label_result_d = Label(root, textvariable=result_d)
label_result_c = Label(root, textvariable=result_c)
label_result_s = Label(root, textvariable=result_s)

# 创建按钮
button_calculate = Button(root, text="计算", command=calculate)

# 添加到界面上，并使内容在程序中心显示
label_r.grid(row=0, column=0, padx=10, pady=5)
entry_r.grid(row=0, column=1, padx=10, pady=5)
label_d.grid(row=1, column=0, padx=10, pady=5)
entry_d.grid(row=1, column=1, padx=10, pady=5)
label_c.grid(row=2, column=0, padx=10, pady=5)
entry_c.grid(row=2, column=1, padx=10, pady=5)
label_s.grid(row=3, column=0, padx=10, pady=5)
entry_s.grid(row=3, column=1, padx=10, pady=5)
label_pi.grid(row=4, column=0, padx=10, pady=5)
entry_pi.grid(row=4, column=1, padx=10, pady=5)

label_result_r.grid(row=0, column=2, padx=10, pady=5)
label_result_d.grid(row=1, column=2, padx=10, pady=5)
label_result_c.grid(row=2, column=2, padx=10, pady=5)
label_result_s.grid(row=3, column=2, padx=10, pady=5)

button_calculate.grid(row=5, column=1, pady=10)

# 运行主循环
root.mainloop()
