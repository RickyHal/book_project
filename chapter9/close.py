# close.py
import os

f = os.open('test.txt', os.O_RDONLY | os.O_CREAT)
os.write(f, str.encode('success!'))
os.close(f)
print('success!')
