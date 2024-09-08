import os
import sys
import subprocess
from plyer import notification

def main():
    try:
        subprocess.run(['clip'], input=os.path.dirname(os.path.abspath(sys.argv[0])).strip().encode('utf-8'), check=True)
        notification.notify(
            title='芙芙工具箱 | 开发工具',
            message=f'成功将开发工具路径复制到剪贴板！',
            timeout=3
        )
        return 0
    except Exception as e:
        notification.notify(
            title='芙芙工具箱 | 开发工具',
            message=f'由于以下原因无法将路径复制到剪切板:\n{e}',
            timeout=3
        )
        return 1

if __name__ == "__main__":
    sys.exit(main())
