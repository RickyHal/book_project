# f_open_close.py
#!/usr/bin/env python3

# 打开当前目录的file_1.txt文件
f1 = open('file_1.txt')
f2 = open('./file_1.txt')
# 打开上一层目录的file_2.txt文件
f3 = open('../file_2.txt')
print(f1)
print(f2)
print(f3)
# 关闭文件
f1.close()
f2.close()
f3.close()
