# reduce_sum.py
#!/usr/bin/env python3
from functools import reduce


def list_sum(x, y):
    return x + y

l = [1, 2, 3]
print((reduce(list_sum, l)))
