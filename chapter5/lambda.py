# lambda.py
#!/usr/bin/env python3
from functools import reduce

l = [1, 1.5, 2, 3]
print(list(filter(lambda x: isinstance(x, float), l)))
print(list(map(lambda x: x**2, l)))
print(reduce(lambda x, y: x + y, l))
