# func_args_9.py
#!/usr/bin/env python3


def print_kv(**args):
    print('传入的参数', args)
    for key, value in args.items():
        print('%s=%d' % (key, value))

print_kv(num1=1, num2=2, num3=3, num4=4, num5=5)
