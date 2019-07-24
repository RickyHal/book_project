# return_many.py
#!/usr/bin/env python3


def return_many():
    # 返回多个值
    return 1, 2.1, 'hello world'

data = return_many()
print(type(data))
for item in data:
    print(item)
