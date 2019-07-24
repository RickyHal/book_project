# sep_linesep.py
import os

path = '.' + os.sep + 'testCode' + os.sep + 'test.txt'
if os.path.exists('testCode') == False:  # 目录不存在
    os.makedirs('testCode')  # 创建目录testCode
f = os.open(path, os.O_WRONLY | os.O_CREAT)  # 在testCode目录下打开或创建文件test.txt
os.write(f, str.encode('hello' + os.linesep + "world"))  # 写入有换行的文本
os.close(f)
f1 = os.open(path, os.O_RDONLY | os.O_CREAT)  # 读出写入的文本
string = os.read(f1, 20)
print(string)
os.close(f1)
