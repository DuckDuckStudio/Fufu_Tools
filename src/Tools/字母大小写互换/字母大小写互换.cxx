#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main () {
    string a; // 存储用于大小写转换的输入字符串
    cout << "请输入需要转换的字符: ";
    getline(cin, a);

    for (int i=0; a[i]; i++) {
        if (islower(a[i])) {
            a[i] = toupper(a[i]);
        } else if (isupper(a[i])) {
            a[i] = tolower(a[i]);
        } 
    }
    cout << "转换结果为: " << a << endl << endl;
    system("pause"); 
    return 0;
}
