import datetime
from datetime import date
import multiprocessing

now = date.today()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
    print(now_str, file=output)

with open('today.txt', 'rt') as input:
    today_string = input.read()

fmt = '%Y-%m-%d\n'
datetime.datetime.strptime(today_string, fmt)


def now(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())

if __name__ == '__main__':
    import random
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=now, args=(seconds,))
        proc.start()