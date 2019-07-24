# create_threading_eg.py
import threading
import time


class myThread(threading.Thread):

    def __init__(self):
        super(myThread, self).__init__()

    def run(self):  # 定义run方法
        print('线程：' + self.getName() + '开始 ' + time.ctime(time.time()))
        time.sleep(2)
        print('线程:' + self.getName() + '结束 ' + time.ctime(time.time()))


if __name__ == '__main__':
    print('主线程开始时间：', time.ctime(time.time()))
    # 创建线程
    thread = myThread()
    # 设置线程名称
    thread.setName('Thread-1')
    thread.setDaemon(True)
    thread.start()
    time.sleep(1)
    print('主线程结束时间：', time.ctime(time.time()))
