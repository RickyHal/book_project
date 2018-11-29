# getFileTime.py
import os
import time  # 引入time模块将返回的浮点型秒数转换成易于查看的时间

path = 'C:\\Users\\1\\test.txt'
f = os.open(path, os.O_WRONLY | os.O_CREAT)
print('文件创建时间', time.ctime(os.path.getctime(path)))  # 文件创建时间
os.write(f, str.encode('test file'))
print('文件最近修改时间', time.ctime(os.path.getmtime(path)))  # 文件最近修改时间
os.close(f)
f = os.open(path, os.O_RDONLY | os.O_CREAT)
print(os.read(f, 100))
print('文件最近访问时间', time.ctime(os.path.getatime(path)))  # 文件最近访问时间
os.close(f)  # 关闭文件
