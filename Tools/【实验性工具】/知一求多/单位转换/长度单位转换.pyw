from tkinter import *
from tkinter import messagebox

# 定义计算函数
def calculate():
    input_fields = [entry_nanometer, entry_micrometer, entry_millimeter, entry_centimeter, entry_meter,
                    entry_kilometer, entry_inch, entry_foot, entry_yard, entry_mile, entry_nautical_mile]
    input_values = [float(entry.get()) if entry.get() else None for entry in input_fields]

    if sum(value is not None for value in input_values) != 1:
        messagebox.showerror("错误", "请且只能输入一个参数！")
    else:
        try:
            nanometer, micrometer, millimeter, centimeter, meter, kilometer, inch, foot, yard, mile, nautical_mile = input_values
            
            if nanometer is not None:
                micrometer = nanometer / 1000
                millimeter = nanometer / 1000000
                centimeter = nanometer / 10000000
                meter = nanometer / 1000000000
                kilometer = nanometer / 1000000000000
                inch = nanometer / 25400000
                foot = nanometer / 304800000
                yard = nanometer / 914400000
                mile = nanometer / 1609344000000
                nautical_mile = nanometer / 1852000000000

            elif micrometer is not None:
                nanometer = micrometer * 1000
                millimeter = micrometer / 1000
                centimeter = micrometer / 10000
                meter = micrometer / 1000000
                kilometer = micrometer / 1000000000
                inch = micrometer / 25400
                foot = micrometer / 304800
                yard = micrometer / 914400
                mile = micrometer / 1609344000
                nautical_mile = micrometer / 1852000000

            elif millimeter is not None:
                nanometer = millimeter * 1000000
                micrometer = millimeter * 1000
                centimeter = millimeter / 10
                meter = millimeter / 1000
                kilometer = millimeter / 1000000
                inch = millimeter / 25.4
                foot = millimeter / 304.8
                yard = millimeter / 914.4
                mile = millimeter / 1609344
                nautical_mile = millimeter / 1852000

            elif centimeter is not None:
                nanometer = centimeter * 10000000
                micrometer = centimeter * 10000
                millimeter = centimeter * 10
                meter = centimeter / 100
                kilometer = centimeter / 100000
                inch = centimeter / 2.54
                foot = centimeter / 30.48
                yard = centimeter / 91.44
                mile = centimeter / 160934.4
                nautical_mile = centimeter / 185200

            elif meter is not None:
                nanometer = meter * 1000000000
                micrometer = meter * 1000000
                millimeter = meter * 1000
                centimeter = meter * 100
                kilometer = meter / 1000
                inch = meter * 39.37
                foot = meter * 3.281
                yard = meter * 1.094
                mile = meter / 1609.344
                nautical_mile = meter / 1852

            elif kilometer is not None:
                nanometer = kilometer * 1000000000000
                micrometer = kilometer * 1000000000
                millimeter = kilometer * 1000000
                centimeter = kilometer * 100000
                meter = kilometer * 1000
                inch = kilometer * 39370.1
                foot = kilometer * 3280.84
                yard = kilometer * 1093.61
                mile = kilometer / 1.609
                nautical_mile = kilometer / 1.852

            elif inch is not None:
                nanometer = inch * 25400000
                micrometer = inch * 25400
                millimeter = inch * 25.4
                centimeter = inch * 2.54
                meter = inch / 39.37
                kilometer = inch / 39370.1
                foot = inch / 12
                yard = inch / 36
                mile = inch / 63360
                nautical_mile = inch / 72913.4

            elif foot is not None:
                nanometer = foot * 304800000
                micrometer = foot * 304800
                millimeter = foot * 304.8
                centimeter = foot * 30.48
                meter = foot / 3.281
                kilometer = foot / 3280.84
                inch = foot * 12
                yard = foot / 3
                mile = foot / 5280
                nautical_mile = foot / 6076.12

            elif yard is not None:
                nanometer = yard * 914400000
                micrometer = yard * 914400
                millimeter = yard * 914.4
                centimeter = yard * 91.44
                meter = yard / 1.094
                kilometer = yard / 1093.61
                inch = yard * 36
                foot = yard * 3
                mile = yard / 1760
                nautical_mile = yard / 2025.37

            elif mile is not None:
                nanometer = mile * 1609344000000
                micrometer = mile * 1609344000
                millimeter = mile * 1609344
                centimeter = mile * 160934.4
                meter = mile * 1609.344
                kilometer = mile * 1.609
                inch = mile * 63360
                foot = mile * 5280
                yard = mile * 1760
                nautical_mile = mile / 1.151

            elif nautical_mile is not None:
                nanometer = nautical_mile * 1852000000000
                micrometer = nautical_mile * 1852000000
                millimeter = nautical_mile * 1852000
                centimeter = nautical_mile * 185200
                meter = nautical_mile * 1852
                kilometer = nautical_mile * 1.852
                inch = nautical_mile * 72913.4
                foot = nautical_mile * 6076.12
                yard = nautical_mile * 2025.37
                mile = nautical_mile * 1.151

            result_nanometer.set(nanometer)
            result_micrometer.set(micrometer)
            result_millimeter.set(millimeter)
            result_centimeter.set(centimeter)
            result_meter.set(meter)
            result_kilometer.set(kilometer)
            result_inch.set(inch)
            result_foot.set(foot)
            result_yard.set(yard)
            result_mile.set(mile)
            result_nautical_mile.set(nautical_mile)

            for entry in input_fields:
                entry.delete(0, END)

        except ValueError:
            messagebox.showerror("错误", "请输入有效数字！")

# 创建主窗口
root = Tk()
root.title("长度单位转换器")

# 创建标签和输入框
label_nanometer = Label(root, text="纳米：")
entry_nanometer = Entry(root)
label_micrometer = Label(root, text="微米：")
entry_micrometer = Entry(root)
label_millimeter = Label(root, text="毫米：")
entry_millimeter = Entry(root)
label_centimeter = Label(root, text="厘米：")
entry_centimeter = Entry(root)
label_meter = Label(root, text="米：")
entry_meter = Entry(root)
label_kilometer = Label(root, text="公里：")
entry_kilometer = Entry(root)
label_inch = Label(root, text="英寸：")
entry_inch = Entry(root)
label_foot = Label(root, text="英尺：")
entry_foot = Entry(root)
label_yard = Label(root, text="码：")
entry_yard = Entry(root)
label_mile = Label(root, text="英里：")
entry_mile = Entry(root)
label_nautical_mile = Label(root, text="海里：")
entry_nautical_mile = Entry(root)

# 创建结果标签
result_nanometer = StringVar()
result_micrometer = StringVar()
result_millimeter = StringVar()
result_centimeter = StringVar()
result_meter = StringVar()
result_kilometer = StringVar()
result_inch = StringVar()
result_foot = StringVar()
result_yard = StringVar()
result_mile = StringVar()
result_nautical_mile = StringVar()

label_result_nanometer = Label(root, textvariable=result_nanometer)
label_result_micrometer = Label(root, textvariable=result_micrometer)
label_result_millimeter = Label(root, textvariable=result_millimeter)
label_result_centimeter = Label(root, textvariable=result_centimeter)
label_result_meter = Label(root, textvariable=result_meter)
label_result_kilometer = Label(root, textvariable=result_kilometer)
label_result_inch = Label(root, textvariable=result_inch)
label_result_foot = Label(root, textvariable=result_foot)
label_result_yard = Label(root, textvariable=result_yard)
label_result_mile = Label(root, textvariable=result_mile)
label_result_nautical_mile = Label(root, textvariable=result_nautical_mile)

# 创建按钮
button_calculate = Button(root, text="计算", command=calculate)

# 添加到界面上，并使内容在程序中心显示
label_nanometer.grid(row=0, column=0, padx=10, pady=5)
entry_nanometer.grid(row=0, column=1, padx=10, pady=5)
label_micrometer.grid(row=1, column=0, padx=10, pady=5)
entry_micrometer.grid(row=1, column=1, padx=10, pady=5)
label_millimeter.grid(row=2, column=0, padx=10, pady=5)
entry_millimeter.grid(row=2, column=1, padx=10, pady=5)
label_centimeter.grid(row=3, column=0, padx=10, pady=5)
entry_centimeter.grid(row=3, column=1, padx=10, pady=5)
label_meter.grid(row=4, column=0, padx=10, pady=5)
entry_meter.grid(row=4, column=1, padx=10, pady=5)
label_kilometer.grid(row=5, column=0, padx=10, pady=5)
entry_kilometer.grid(row=5, column=1, padx=10, pady=5)
label_inch.grid(row=6, column=0, padx=10, pady=5)
entry_inch.grid(row=6, column=1, padx=10, pady=5)
label_foot.grid(row=7, column=0, padx=10, pady=5)
entry_foot.grid(row=7, column=1, padx=10, pady=5)
label_yard.grid(row=8, column=0, padx=10, pady=5)
entry_yard.grid(row=8, column=1, padx=10, pady=5)
label_mile.grid(row=9, column=0, padx=10, pady=5)
entry_mile.grid(row=9, column=1, padx=10, pady=5)
label_nautical_mile.grid(row=10, column=0, padx=10, pady=5)
entry_nautical_mile.grid(row=10, column=1, padx=10, pady=5)

label_result_nanometer.grid(row=0, column=2, padx=10, pady=5)
label_result_micrometer.grid(row=1, column=2, padx=10, pady=5)
label_result_millimeter.grid(row=2, column=2, padx=10, pady=5)
label_result_centimeter.grid(row=3, column=2, padx=10, pady=5)
label_result_meter.grid(row=4, column=2, padx=10, pady=5)
label_result_kilometer.grid(row=5, column=2, padx=10, pady=5)
label_result_inch.grid(row=6, column=2, padx=10, pady=5)
label_result_foot.grid(row=7, column=2, padx=10, pady=5)
label_result_yard.grid(row=8, column=2, padx=10, pady=5)
label_result_mile.grid(row=9, column=2, padx=10, pady=5)
label_result_nautical_mile.grid(row=10, column=2, padx=10, pady=5)

button_calculate.grid(row=11, column=1, pady=10)

# 运行主循环
root.mainloop()
