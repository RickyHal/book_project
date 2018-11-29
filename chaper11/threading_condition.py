# threading_condition.py
import threading
import time


# 用户


class User(threading.Thread):

    def __init__(self, name, lock):
        super(User, self).__init__()
        self.name = name
        self.lock = lock

    def run(self):
        # 申请锁
        self.lock.acquire()

        print(time.ctime(time.time()), self.name + ': 你好')

        # 等待回答
        self.lock.wait()
        print(time.ctime(time.time()), self.name + ': 我想办个会员')
        # 通知客服可以回答了
        self.lock.notify()

        self.lock.wait()
        print(time.ctime(time.time()), self.name + ': 好的谢谢')
        self.lock.notify()

        # 释放锁
        self.lock.release()


# 客服


class Service(threading.Thread):

    def __init__(self, name, lock):
        super(Service, self).__init__()
        self.name = name
        self.lock = lock

    def run(self):
        # 申请锁
        self.lock.acquire()

        # 唤醒回答
        self.lock.notify()
        time.sleep(2)
        print(time.ctime(time.time()), self.name + ': 你好')
        # 通知用户可以发消息了
        self.lock.wait()

        self.lock.notify()
        time.sleep(2)
        print(time.ctime(time.time()), self.name + ': 好的马上为您办理')
        self.lock.wait()

        self.lock.notify()
        time.sleep(2)
        print(time.ctime(time.time()), self.name + ': 已为您办理会员')

        # 释放锁
        self.lock.release()


if __name__ == "__main__":
    lock = threading.Condition()
    ask = User('用户', lock)
    answer = Service('客服', lock)
    print('****开始****')
    ask.start()
    answer.start()
