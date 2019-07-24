# process_pool.py
from multiprocessing import Pool
import os
import time

# 定义子进程执行的函数


def childProcess(process_name):
    print('%s start,pid=%s |now time is %s' %
          (process_name, os.getpid(), time.ctime(time.time())))
    time.sleep(2)
    print('%s stop,pid=%s |now time is %s' %
          (process_name, os.getpid(), time.ctime(time.time())))

# 主进程


def main():
    print('main process start,pid=%s  |now time is %s' %
          (os.getpid(), time.ctime(time.time())))
    # 创建进程池
    p = Pool(3)
    for i in range(3):
        # 向进程池添加子进程
        p.apply_async(childProcess, args=('child process-' + str(i),))
    # 关闭进程池，关闭后不可再添加子进程
    p.close()
    # 调用join函数之前必须调用close函数关闭进程池
    p.join()
    print('main process stop,pid=%s  |now time is %s' %
          (os.getpid(), time.ctime(time.time())))

if __name__ == "__main__":
    main()
