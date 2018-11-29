# lock_thread.py
import _thread
import time
import sys


# 创建线程函数


def t_func(t_name, count, lock):
    while count > 0:
        # 线程休眠1秒
        time.sleep(1)
        print('当前运行线程：' + t_name + ' id: ' +
              str(_thread.get_ident()) + '  ' + time.ctime(time.time()))
        count -= 1
    print('线程' + t_name + '运行结束： ' + time.ctime(time.time()))
    # 释放锁
    lock.release()


# 创建main函数


def main():
    try:
        print('主线程开始时间：', time.ctime(time.time()))
        locks = []
        for i in range(1, 4):
            # 分配锁对象
            lock = _thread.allocate_lock()
            # 获取锁
            lock.acquire()
            locks.append(lock)
            # 创建线程
            _thread.start_new_thread(t_func, ('Thread-' + str(i), i, lock))
        # 检测锁
        for i in locks:
            # 判断锁是否释放
            while i.locked():
                pass
        print('主线程结束时间：', time.ctime(time.time()))
    except Exception as e:
        print('线程启动失败：' + str(e))
        sys.exit(0)


if __name__ == '__main__':
    main()
