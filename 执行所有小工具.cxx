#include <iostream>
#include <windows.h>

using namespace std;

int main()
{
    //获取C++文件所在目录
    char chpath [MAX_PATH];
    GetModuleFileName (NULL, ( LPSTR)chpath,sizeof (chpath));
    string strPath = chpath;
    strPath = strPath.substr(0, strPath.rfind('\\'));

    //执行 清C盘缓存.bat
    system((strPath + "\\bat\\清C盘缓存.bat").c_str());
    
    //返回0
    return 0;
}
