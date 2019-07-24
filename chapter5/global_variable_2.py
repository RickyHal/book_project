# global_variable_2.py
#!/usr/bin/env python3

x = 1


def change_x():
    global x
    print('函数内改变前x =', x)
    x = 7
    print('函数内改变后x =', x)

change_x()
print('执行函数后x =', x)
