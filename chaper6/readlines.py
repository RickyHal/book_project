# readlines.py
#!/usr/bin/env python3

file = open('file_2.txt', 'r')
# 读取文件中的所有内容，并以列表的形式返回
lines = file.readlines()
print(lines)
for line in lines:
    print(line)
file.close()
