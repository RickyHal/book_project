# lseek.py
import os

f = os.open('test.txt', os.O_RDWR | os.O_CREAT)
os.write(f, str.encode('123a 56 bb'))
# 从开始位置读取字符串
os.lseek(f, 0, 0)
print("已写入：", os.read(f, 10))
# 从位置5开始读取字符串
os.lseek(f, 5, 0)
print("5之后的字符串：", os.read(f, 10))
os.close(f)
