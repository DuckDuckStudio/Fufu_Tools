#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

int main() {
    string file_name;
    string file_format;
    string file_size;
    string file_route;

    cout << "��������Ҫ���ɵ��ļ���(��Ҫ�Ӻ�׺��): ";
    cin >> file_name;

    cout << "��������Ҫ���ɵ��ļ��ĸ�ʽ(����.exe): ";
    cin >> file_format;

    cout << "��������Ҫ���ɵ��ļ��Ĵ�С(��BΪ��λ): ";
    cin >> file_size;

    cout << "��������Ҫ�����ļ���·��(����D:\\)[������\"\\\"��β�����ܴ�����]: ";
    cin >> file_route;

    cout << "����������ȫ���ռ���ϣ�" << endl;
    cout << "�ļ���������..." << endl;

    string file_complete_name = file_name + file_format;
    string file_complete_route = file_route + file_complete_name;

    ofstream file(file_complete_route.c_str(), ios::binary);
    file.seekp(atoi(file_size.c_str()) - 1);
    file.write("", 1);
    file.close();

    // �ж��ļ��Ƿ���ȷ����
    ifstream check_file(file_complete_route.c_str());
    if (check_file) {
        cout << "��ϲ�㣬�ļ����ɳɹ���" << endl;
    } else {
        cout << "�ܱ�Ǹ���ļ�����ʧ�ܣ�����Գ�����������������" << endl;
        cout << "��Ȼ�������֪����������������ṩ���õģ�������ύ��Issues��" << endl;
    }

    cout << "����������ϣ�" << endl;
    system("pause");
    return 0;
}
