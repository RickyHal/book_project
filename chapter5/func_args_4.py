# func_args_4.py
#!/usr/bin/env python3


def func_a(x, func):
    func(x)


def func_b(x):
    print(x)


func_a('hello world', func_b)
