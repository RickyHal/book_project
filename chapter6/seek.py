# seek.py
#!/usr/bin/env python3

file = open('file_2.txt', 'r')
# 读取第一行
print(file.readline())
# 读取第二行
print(file.readline())
# 将指针移到第一行
file.seek(0)
# 读取第一行
print(file.readline())
# 读取第二行
print(file.readline())
file.close()
