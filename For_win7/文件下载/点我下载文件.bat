@echo off

echo --������ʹ��Powershell--
echo ע�⣺�������޷�ֱ�����ص��ļ�(����xx����)ʱ���ܻ��޷����أ�

set /p file_route="����������Ҫ���ļ����ص��ĸ��ļ��У�"
cd /d %file_route%
 
set /p exename="����������Ҫ�����غ���ļ�����Ϊʲô��"
set /p downurl="�������ļ��������ӣ�"

powershell curl -o "%exename%" "%downurl%"

echo ������ɣ�

pause