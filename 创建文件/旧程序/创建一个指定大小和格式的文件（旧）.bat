@echo off
REM �رջ���
REM chcp 65001
REM ʹ��UTF-8����
REM ��ʼ�����

:set_name
set /p file_name="��������Ҫ���ɵ��ļ���(��Ҫ�Ӻ�׺��):"
REM ��ȡ%file_name%(�����ļ���)

set /p file_format="��������Ҫ���ɵ��ļ��ĸ�ʽ(����.exe):"
REM ��ȡ%file_format%(�����ļ���ʽ)

set /p file_size="��������Ҫ���ɵ��ļ��Ĵ�С(��BΪ��λ):"
REM ��ȡ%file_size%(�����ļ���С)

set /p file_route="��������Ҫ�����ļ���·��(����D:\)[�����ԡ�\����β�����ܴ�����]:"
REM ��ȡ%file_route%(�����ļ�·��)
echo ����������ȫ���ռ���ϣ�

echo �ļ���������...
REM �����ļ�
set file_complete_name=%file_name%%file_format%
set file_complete_route=%file_route%%file_complete_name%

pushd %file_route%
fsutil file createnew %file_complete_route% %file_size%
popd

REM �ж��ļ��Ƿ���ȷ����
if exist %file_complete_route% (
    echo ��ϲ�㣬�ļ����ɳɹ���
) else (
    echo �ܱ�Ǹ���ļ�����ʧ�ܣ�����Գ�����������������
    echo ��Ȼ�������֪����������������ṩ���õģ�������ύ��Issues��
)

echo ����������ϣ�
pause
