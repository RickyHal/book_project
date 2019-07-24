# read_2.py
#!/usr/bin/env python3

file = open('file_2.txt', 'r')
# 读取6字节内容
print(file.read(6))
file.close()
