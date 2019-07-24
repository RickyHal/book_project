# write.py
import os

f = os.open('test.txt', os.O_RDWR | os.O_CREAT)
os.write(f, str.encode('hello'))
os.close(f)
print('success!')
