# thread_process.py
import random
import threading
from multiprocessing import Process

# 定义线程


class myThread(threading.Thread):

    def __init__(self, process_name):
        super(myThread, self).__init__()
        self.process_name = process_name

    def run(self):
        print('\tI am thread %s,and I belong to process %s' %
              (self.getName(), self.process_name))

# 定义进程


class MyProcess(Process):

    def __init__(self, process_name):
        super(MyProcess, self).__init__()
        self.process_name = process_name

    def run(self):
        # 创建2个线程
        for i in range(2):
            thread = myThread(self.process_name)
            thread_name = 'Thread-' + str((random.randint(0, 9999)))
            thread.setName(thread_name)
            print('I am child process %s and I create a thread %s' %
                  (self.process_name, thread_name))
            thread.start()

if __name__ == "__main__":
    # 创建2个进程
    for i in range(2):
        process_name = 'Process-' + str((i + 1))
        process = MyProcess(process_name)
        process.start()
        print('I am main process and I create a child process %s' %
              (process_name))
