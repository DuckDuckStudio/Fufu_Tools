#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// Function to read config.ini file
void readConfigFile(string& mvn, string& sorn) {
    ifstream configFile("config.ini");
    if (configFile.is_open()) {
        string line;
        while (getline(configFile, line)) {
            if (line.find("major_version_number") != string::npos) {
                mvn = line.substr(line.find("=") + 2);
            } else if (line.find("status_or_revision_number") != string::npos) {
                sorn = line.substr(line.find("=") + 2);
            }
        }
        configFile.close();
    }
}

int main() {
    string mvn, sorn;
    readConfigFile(mvn, sorn);

    // Output
    cout << "--------------芙芙工具箱--------------" << endl;
    cout << "-> Code by 鸭鸭「カモ」/ DuckStudio" << endl;
    cout << "Version: v" << mvn << "-" << sorn << endl;
    cout << "-------------------------------------" << endl;

    system("pause");
    
    return 0;
}
