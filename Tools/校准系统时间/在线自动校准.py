import ntplib
from time import ctime
import datetime

def sync_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('time.windows.com') # 使用Windows time服务器
        local_time = ctime(response.tx_time)
        print("校准前本地时间：", ctime())
        print("开始校准时间...")
        new_time = datetime.datetime.strptime(local_time, "%a %b %d %H:%M:%S %Y")
        datetime.datetime.now().replace(year=new_time.year, month=new_time.month, day=new_time.day,
                                        hour=new_time.hour, minute=new_time.minute, second=new_time.second)
        print("校准后本地时间：", ctime())
    except ImportError as e:
        print("导入模块失败：", str(e))
    except ntplib.NTPException as e:
        print("无法连接到NTP服务器：", str(e))
    except Exception as e:
        print("时间校准失败：", str(e))

if __name__ == '__main__':
    sync_time()

input("按Enter键继续...")
