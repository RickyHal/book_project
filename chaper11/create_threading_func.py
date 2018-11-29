# create_threading_func.py
import threading


def func(parameter):


# 函数体
thread = threading.Thread(target=func, args=(parameter))
