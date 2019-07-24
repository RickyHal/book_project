# process_queue.py
import time
from multiprocessing import Process, Queue

q = Queue(3)

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
    # 写元素进程
    write = Process(target=putItem, args=(q,))
    # 读元素进程
    read = Process(target=getItem, args=(q,))
    write.start()
    print('write start')
    read.start()
    print('read start')
if __name__ == "__main__":
    main()
