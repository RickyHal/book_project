# create_threading_func.py
import threading


def func(parameter):
    pass

# 函数体
thread = threading.Thread(target=func, args=(parameter))
