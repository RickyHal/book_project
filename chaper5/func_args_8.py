# func_args_8.py
#!/usr/bin/env python3


def calculate_sum(*numbers):
    print('传入的参数', numbers)
    print('sum=', sum(numbers))

calculate_sum(1, 2, 3, 4, 5)
