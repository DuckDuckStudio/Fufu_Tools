@echo off
echo ���Ը���pip...
echo -------------------
python.exe -m pip install --upgrade pip
���½���
echo -------------------
echo ��ʼ��װ���ļ�...
REM ---
echo -------------------
echo ���ڰ�װ�� translate
pip install translate
echo ��װ�� translate ����
echo -------------------
echo ���ڰ�װ�� requests
pip install requests
echo ��װ�� requests ����
echo -------------------
echo ���ڰ�װ�� beautifulsoup4
pip install beautifulsoup4
echo ��װ�� beautifulsoup4 ����
REM skip to install "requests"
echo -------------------
echo ���ڰ�װ�� webbrowser
pip install webbrowser
echo ��װ�� webbrowser ����
REM skip to install "webbrowser"
echo -------------------
echo ���ڰ�װ�� ntplib
pip install ntplib
echo ��װ�� ntplib ����
echo -------------------
echo ���ڰ�װ�� tqdm
pip install tqdm
echo ��װ�� tqdm ����
echo -------------------
echo ����������ļ���װ��ɣ�
echo ������������Խ����������������������һ���ύIssues��
echo ����ؼ���ERROR�����п�����ȷ�Ͽ��ļ���װ�����
echo �������������ʹ�÷��������
pause
