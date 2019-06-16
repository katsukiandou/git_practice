import schedule
from datetime import datetime as dt
import time
def heavy_process():
    res = 2
    for i in range(10**5):
        res += i
    print(res)


def job():
    base_time = dt.now()
    print(time)
    heavy_process()


if __name__ == '__main__':
    start = dt.now()

