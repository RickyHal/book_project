# yield.py
#!/usr/bin/env python3


def return_num():
    for i in range(5):
        yield i

# data为迭代器，由返回的生成器实现
data = return_num()
print(type(data))
# 输出下一个迭代元素
print('next', next(data))
# 遍历输出元素
for i in data:
    print(i)
