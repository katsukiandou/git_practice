from datetime import datetime as dt
import time

def heavy_process():
    res = 0
    for i in range(10**7):
        res += i
    print(res)

##定期実行のためのプロセス
a = 2
while True:
    start_ = dt.now()
    print(start_)

    heavy_process()
    process_time = dt.now() - start_
    print(process_time)
    process_time = round(process_time.total_seconds(), 3)
    time.sleep(60 - process_time)