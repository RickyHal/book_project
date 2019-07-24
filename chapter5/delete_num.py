# delete_num.py
#!/usr/bin/env python3


def delete_num(x):
    # 如果当前元素不是浮点数
    return not isinstance(x, float)

l = [1, 1.5, 2, 2.5, 3]
print(list(filter(delete_num, l)))
