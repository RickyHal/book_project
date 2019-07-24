# process_pool_queue.py
import time
import os
from multiprocessing import Pool, Manager, Queue

# 向队列写入元素


def putItem(q):
    while 1:
        if not q.full():
            q.put('Python')
            print('%s put string:Python |now size is %s' %
                  (time.ctime(time.time()), str(q.qsize())))
        else:
            print('queue is full')
            break
        time.sleep(1)

# 读取元素


def getItem(q):
    while 1:
        if not q.empty():
            print('%s get string:%s |now size is %s' %
                  (time.ctime(time.time()), q.get(), q.qsize()))
        else:
            print('queue is empty')
            break
        time.sleep(2)

# 主进程


def main():
    # 创建进程池
    p = Pool(2)
    # 向进程池中加入进程
    p.apply_async(putItem, args=(q,))
    p.apply_async(getItem, args=(q,))
    p.close()
    p.join()

if __name__ == "__main__":
    q = Manager().Queue(2)
    main()
