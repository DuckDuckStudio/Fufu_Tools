#include <iostream>
using namespace std;

char a[114514];

int main () {
    cout << "请输入需要转换的字符：";
	cin >> a;
    //---
	for (int i=0;a[i];i++) {
		if (a[i] >= 'a'&&a[i] <= 'z') {
			a[i] -= 32;
		} else if (a[i] >= 'A'&&a[i] <= 'Z') {
			a[i] += 32;
		} 
	}
	//---
    cout << "转换结果为：";
	for (int i=0;a[i];i++) {
		cout << a[i];
	}
	
	cout << endl << endl;
	system("pause"); 
	return 0;
}
