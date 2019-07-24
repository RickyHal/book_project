# local_variable_2.py
#!/usr/bin/env python3


def change_or_not(x):
    print('初始 x 的值为', x)
    x = 7
    print('改变 x 的值为', x)

x = 1
change_or_not(x)
print('函数执行完 x 的值为', x)
