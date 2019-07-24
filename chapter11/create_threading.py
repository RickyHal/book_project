# create_threading_eg.py
import threading
import time


class myThread(threading.Thread):

    def __init__(self, i):
        super(myThread, self).__init__()
        self.i = i

    def run(self):  # 定义run方法
        print('线程：' + self.getName() + '开始 ' + time.ctime(time.time()))
        time.sleep(i)
        print('线程:' + self.getName() + '结束 ' + time.ctime(time.time()))


if __name__ == '__main__':
    print('主线程开始时间：', time.ctime(time.time()))
    # 创建线程列表
    threads = []
    for i in range(1, 4):
        thread = myThread(i)
        # 设置线程名称
        thread.setName('Thread-' + str(i))
        threads.append(thread)
    # 启动线程
    for thread in threads:
        thread.start()
        thread.join(1)
    print('主线程结束时间：', time.ctime(time.time()))
