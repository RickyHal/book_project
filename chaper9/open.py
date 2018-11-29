# open.py
import os

f = os.open('test.txt', os.O_RDWR | os.O_CREAT)
print(os.stat(f))
os.close(f)
