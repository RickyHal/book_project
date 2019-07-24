# threading_lock.py
import threading
import time

# 全局变量
num = 0
# 申请锁
lock = threading.Lock()


class Count(threading.Thread):

    def __init__(self):
        super(Count, self).__init__()

    def run(self):  # 定义run方法
        global num
        # 以下注释为加锁部分
        lock.acquire()
        while num < 5:
            time.sleep(2)
            print('线程：' + self.getName(), 'num:', num)
            num += 1
        lock.release()


if __name__ == '__main__':
    print('主线程开始时间：', time.ctime(time.time()))
    thread1 = Count()
    thread2 = Count()
    # 设置线程名称
    thread1.setName('Thread-1')
    thread2.setName('Thread-2')
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('主线程结束时间：', time.ctime(time.time()))
