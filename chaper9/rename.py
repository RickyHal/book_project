# rename.py
import os

# 重命名文件
os.rename('test.txt', 'test1.txt')
print('重命名成功')
# 移动文件
os.rename('test1.txt', '../test.txt')
print('移动文件成功')
