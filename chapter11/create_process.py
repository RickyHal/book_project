# create_process.py
from multiprocessing import Process

# 必须继承Process


class MyProcess(Process):
    # args为传入进程的参数，可为多个

    def __init__(self, args):
        # 初始化进程，也可使用下行注释的方法
        super(MyProcess, self).__init__()
        # Process.__init__(self)
        self.args = args

    def run(self):
        # 进程执行的内容
