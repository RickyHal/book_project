# threading_RLock.py
import threading
import time

'''
#申请Lock锁
lock = threading.Lock() 
lock.acquire()
#打印正在运行的线程的列表
print(threading.enumerate())
# 再次申请时产生了死锁。
lock.acquire() 
print(threading.enumerate())
lock.release()
lock.release()
'''
# 申请RLock锁
rLock = threading.RLock()
rLock.acquire()
print(threading.enumerate())
# 再次申请程序不会出现死锁
rLock.acquire()
print(threading.enumerate())
rLock.release()
rLock.release()
