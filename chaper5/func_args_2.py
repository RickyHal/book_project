# func_args_2.py
#!/usr/bin/env python3


def modify_num(num):
    print('修改前,num=', num)
    num += 1
    print('修改后,num=', num)

num = 1
modify_num(num)
print('执行函数后,num=', num)
