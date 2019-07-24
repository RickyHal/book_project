# exit.py
import sys
import os


def printExitValue(value):
    print(value)
    sys.exit(0)  # 正常退出


try:
    sys.exit()  # 异常退出
    # os._exit(1)  # 直接退出
    # exit(1)  # 一般用于shell中退出
except SystemExit as e:  # 捕获异常
    printExitValue(e)
