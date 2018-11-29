# create_thread.py
import _thread
import time
import sys


# 创建线程函数


def t_func(t_name, count):
    while count > 0:
        # 线程休眠1秒
        time.sleep(1)
        print('当前运行线程：' + t_name + ' ' + time.ctime(time.time()))
        count -= 1
    print('线程' + t_name + '运行结束： ' + time.ctime(time.time()))


# 创建main函数


def main():
    try:
        print('主线程开始时间：', time.ctime(time.time()))
        _thread.start_new_thread(t_func, ('Thread-1', 2))
        _thread.start_new_thread(t_func, ('Thread-2', 3))
        # 休眠5秒
        time.sleep(5)
        print('主线程结束时间：', time.ctime(time.time()))
    except Exception as e:
        print('线程启动失败：' + str(e))
        sys.exit(0)


if __name__ == '__main__':
    main()
