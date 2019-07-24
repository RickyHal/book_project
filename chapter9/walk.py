# walk.py
import os

for dirpath, dirnames, filenames in os.walk("."):
    # 输出所有文件夹名
    for dirname in dirnames:
        print('目录：', os.path.join(dirpath, dirname))  # 通过join函数连接当前路径和文件夹名
    # 输出所有文件名
    for filename in filenames:
        print('文件', os.path.join(dirpath, filename))  # 通过join函数连接当前路径和文件名
