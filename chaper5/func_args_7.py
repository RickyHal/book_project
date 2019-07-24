# func_args_7.py
#!/usr/bin/env python3


def average_score(A=59, B=59, C=59):
    print('小明三科的平均分是%.2f' % ((A + B + C) / 3))

# 不传入参数
average_score()
# 传入参数
average_score(59, 59, 100)
# 传入指定参数
average_score(C=100)
# 不按顺序传入参数
average_score(C=100, A=59, B=59)
