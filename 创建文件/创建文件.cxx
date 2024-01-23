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

    cout << "请输入你要生成的文件名(不要加后缀名): ";
    cin >> file_name;

    cout << "请输入你要生成的文件的格式(例如.exe): ";
    cin >> file_format;

    cout << "请输入你要生成的文件的大小(以B为单位): ";
    cin >> file_size;

    cout << "请输入你要生成文件的路径(例如D:\\)[必须以\"\\\"结尾，不能带引号]: ";
    cin >> file_route;

    cout << "需求条件已全部收集完毕！" << endl;
    cout << "文件正在生成..." << endl;

    string file_complete_name = file_name + file_format;
    string file_complete_route = file_route + file_complete_name;

    ofstream file(file_complete_route.c_str(), ios::binary);
    file.seekp(atoi(file_size.c_str()) - 1);
    file.write("", 1);
    file.close();

    // 判断文件是否正确生成
    ifstream check_file(file_complete_route.c_str());
    if (check_file) {
        cout << "恭喜你，文件生成成功！" << endl;
    } else {
        cout << "很抱歉，文件生成失败，你可以尝试重新启动本程序。" << endl;
        cout << "当然，如果你知道具体问题或者能提供配置的，你可以提交【Issues】" << endl;
    }

    cout << "程序运行完毕！" << endl;
    system("pause");
    return 0;
}
