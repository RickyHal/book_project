# with_open.py
#!/usr/bin/env python3

with open('file_1.txt', 'r+') as f:
    print(f)


# open函数方式
try:
    f = open('file_1.txt')
    print(f)
except Exception as e:
    print(e)
finally:
    if f:
        f.close()
