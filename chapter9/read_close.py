# read_close.py
import os

f = os.open('test.txt', os.O_RDONLY | os.O_CREAT)
print(os.read(f, 3))
os.close(f)
print('success')
