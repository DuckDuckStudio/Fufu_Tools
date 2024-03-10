# 将输入的数字按照进制转换为十进制
def to_decimal(num, base):
    dec = 0
    num_str = str(num)
    is_negative = False

    if num_str[0] == '-':
        is_negative = True
        num_str = num_str[1:]  # 去除负号

    num_len = len(num_str)

    for i in range(num_len):
        digit = int(num_str[i], base=base) if num_str[i].isalpha() else int(num_str[i])
        dec += digit * (base ** (num_len - 1 - i))

    if is_negative:
        dec = -dec

    return dec

# 将十进制数转换为指定进制
def from_decimal(num, base):
    res = ""
    is_negative = False

    if num < 0:
        is_negative = True
        num = -num

    while num > 0:
        digit = num % base
        ch = chr(ord('a') + digit - 10) if digit >= 10 else str(digit)
        res = ch + res
        num //= base

    if is_negative:
        res = "-" + res

    return res

def tips():
    print("---数字进制转换器---")
    print("->请输入整数！(正负亦可)")
    print()

if __name__ == "__main__":
    tips()
    from_base = int(input("请输入原数进制："))
    num = input("请输入原数：")
    to_base = int(input("请输入转换后进制："))

    if num == "0":
        print("转换结果：0")
    elif from_base <= 0 or to_base <= 0:
        print("错误：进制不合法！")
    else:
        decimal = to_decimal(num, from_base)
        res = from_decimal(decimal, to_base)
        print("转换结果：", res)

    input("按Enter键继续...")