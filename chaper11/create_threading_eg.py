# create_threading_eg.py
import threading


# 必须继承threading.Thread
class threadName(threading.Thread):
    # args为传入线程的参数，可为多个

    def __init__(self, args):
        # 初始化，threadName必须和类名一样
        super(threadName, self).__init__()
        # 也可使用下列注释中的方法初始化
        # threading.Thread.__init__(self)
        self.args = args

    def run(self):  # 定义run方法
        # 线程执行的内容，注意这里如果需要使用传入线程的变量必须要在变量名前加一个"self."否则会报错
