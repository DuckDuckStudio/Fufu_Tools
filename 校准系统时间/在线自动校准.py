import ntplib
from time import ctime

def sync_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        local_time = ctime(response.tx_time)
        print("校准前本地时间：", ctime())
        print("开始校准时间...")
        import os
        command = 'date -s "%s"' % local_time
        os.system(command)
        print("校准后本地时间：", ctime())
    except Exception as e:
        print("时间校准失败：", str(e))

if __name__ == '__main__':
    sync_time()
