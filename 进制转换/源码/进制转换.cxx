#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// 将输入的数字按照进制转换为十进制
int toDecimal(string num, int base) {
    int dec = 0;
    int len = num.length();

    // 判断是否为负数
    bool isNegative = false;
    if (num[0] == '-') {
        isNegative = true;
        num = num.substr(1); // 去除负号
        len--; // 更新长度
    }

    for (int i = 0; i < len; i++) {
        int digit = (num[i] >= 'a') ? (num[i] - 'a' + 10) : (num[i] - '0');
        dec += digit * pow(base, len - 1 - i);
    }

    if (isNegative) {
        dec = -dec; // 负数取相反数
    }

    return dec;
}

// 将十进制数转换为指定进制
string fromDecimal(int num, int base) {
    string res = "";

    // 判断是否为负数
    bool isNegative = false;
    if (num < 0) {
        isNegative = true;
        num = -num; // 取相反数
    }

    while (num > 0) {
        int digit = num % base;
        char ch = (digit >= 10) ? ('a' + digit - 10) : (digit + '0');
        res = ch + res;
        num /= base;
    }

    if (isNegative) {
        res = "-" + res; // 加上负号
    }

    return res;
}

void tips() {
    cout << "---数字进制转换器---" << endl;
    cout << "->请输入整数！(正负亦可)" << endl;
    cout << endl;
}

int main() {
    tips();
    int fromBase, toBase;
    string num;
    cout << "请输入原数进制：";
    cin >> fromBase;
    cout << "请输入原数：";
    cin >> num;
    cout << "请输入转换后进制：";
    cin >> toBase;

    if (num == "0") {
        cout << "转换结果：0" << endl;
    } else if (fromBase <= 0 || toBase <= 0) {
        cout << "错误：进制不合法！" << endl;
    } else {
        // 先将原数转换为十进制，再将十进制转换为目标进制
        int decimal = toDecimal(num, fromBase);
        string res = fromDecimal(decimal, toBase);
        cout << "转换结果：" << res << endl;
    }

    return 0;
}
