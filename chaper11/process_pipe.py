# process_pipe.py
from multiprocessing import Process, Pipe

# 子进程


def childProcess(conn):
        # 接收父进程发送的内容
    print('子进程收到内容：', conn.recv())
    # 向父进程发送数据
    conn.send('Hello I am child process')
    print('子进程发送内容：Hello I am child process')
    conn.close()

# 父进程


def main():
    parent_conn, child_conn = Pipe()
    p = Process(target=childProcess, args=(child_conn,))
    # 向子进程发送数据
    parent_conn.send('Hello I am parent process')
    p.start()
    print('父进程发送内容：Hello I am parent process')
    # 接收子进程发送的数据
    print('父进程收到内容：', parent_conn.recv())
    p.join()
if __name__ == "__main__":
    main()
