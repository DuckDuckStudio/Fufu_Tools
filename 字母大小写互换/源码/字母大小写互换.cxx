#include <iostream>
using namespace std;

char a[114514];

int main () {
    cout << "��������Ҫת�����ַ���";
	cin >> a;
    //---
	for (int i=0;a[i];i++) {
		if (a[i] >= 'a'&&a[i] <= 'z') {
			a[i] -= 32;
		} else if (a[i] >= 'A'&&a[i] <= 'Z') {
			a[i] +=32;
		} 
	}
	//---
    cout << "ת�����Ϊ��";
	for (int i=0;a[i];i++) {
		cout << a[i];
	}
	
	cout << endl << endl;
	system("pause"); 
	return 0;
}
