#!usr/bin/python3
# fork1.py
import os

pid = os.fork()
if pid == 0:
    print('I am the child process,my pid is {0},and my parent is {1}'.format(
        os.getpid(), os.getppid()))
else:
    print('I am the parent process,my pid is {0},and I just create a child process {1}'.format(
        os.getpid(), pid))
