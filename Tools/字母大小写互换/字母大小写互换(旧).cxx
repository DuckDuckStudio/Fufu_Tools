#include <iostream>
using namespace std;

void toggleCase(char str[]) {
    for (int i = 0; str[i] != '\0'; ++i) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            str[i] -= 32; // 小写转大写
        } else if (str[i] >= 'A' && str[i] <= 'Z') {
            str[i] += 32; // 大写转小写
        }
    }
}

int main() {
    char a[114514];

    cout << "请输入需要转换的字符：";
    cin >> a;

    toggleCase(a); // 调用函数进行大小写转换

    cout << "转换结果为：" << a << endl << endl;

    return 0;
}
