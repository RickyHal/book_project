# create_process_func.py
import multiprocessing

# 定义子进程执行的函数


def p_func(string):
    print(string)

if __name__ == "__main__":
    # 创建子进程
    process = multiprocessing.Process(target=p_func, args=('Python',))
    # 启动子进程
    process.start()
