# sell_ticket.py
import threading
import time
import os
# 定义全局变量，表示余票数
TICKET = 15

# 定义售票线程


class booth(threading.Thread):

    def __init__(self, name, lock):
        super(booth, self).__init__()
        self.lock = lock
        self.name = name

    def run(self):
        while True:
            global TICKET
            # 申请锁
            self.lock.acquire()
            if TICKET > 0:
                # 卖出一张票
                TICKET -= 1
                print("%s卖出了第%s张票,余票%s" % (self.name, 15 - TICKET, TICKET))
            else:
                print("票已经卖完了")
                # 结束线程
                os._exit(0)
            # 释放锁
            self.lock.release()
            time.sleep(1)
if __name__ == "__main__":
    lock = threading.Lock()
    for i in range(3):
        thread = booth('booth-' + str((i + 1)), lock)
        thread.start()
