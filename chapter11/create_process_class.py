# create_process_class.py
from multiprocessing import Process

# 定义子进程类


class MyProcess(Process):

    def __init__(self, string):
        super(MyProcess, self).__init__()
        self.string = string

    def run(self):
        print(self.string)

if __name__ == "__main__":
        # 创建子进程
    p = MyProcess('Python')
    # 启动子进程
    p.start()
