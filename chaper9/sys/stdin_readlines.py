# stdin_readlines.py
import sys

sum = 0  # 总和
for item in sys.stdin.readlines():
    sum = sum + int(item)
print('输入数字总和为：' + str(sum))
