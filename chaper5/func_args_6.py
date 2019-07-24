# func_args_6.py
#!/usr/bin/env python3


def print_string(string='hello world', a):
    print(a, string)

# 不传入值，此时打印默认值
print_string('a', 1)
# 传入值，此时打印传入的值
print_string('I am Python3', 1)
