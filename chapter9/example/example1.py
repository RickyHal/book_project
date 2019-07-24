# example1.py
import os
import sys
import time  # 引入time模块将返回的浮点型秒数转换成易于查看的时间


def storeFileDir(path):
    storeFileName = 'example1.txt'  # 存储文件和目录信息的文件
    fileList = []  # 存储文件信息的列表
    dirList = []  # 存储目录信息的列表
    otherList = []  # 存储其它文件信息的列表
    os.chdir(path)  # 更改当前目工作目录
    # 打开文件
    f = os.open(storeFileName, os.O_WRONLY | os.O_CREAT)
    # 写入表头
    os.write(f, str.encode('名称  类型  绝对路径  创建时间  文件大小  \n'))
    # 遍历当前路径文件和目录
    for item in os.listdir():
        if os.path.isfile(item):  # 文件
            # 这里的文件大小单位转换成了kb类型的，并使用了round函数保留了两位小数
            string = item + '  文件  ' + os.path.abspath(item) + '  ' + time.ctime(
                os.path.getctime(item)) + '  ' + str(round(os.path.getsize(item) / 1024, 2)) + 'kb\n'
            fileList.append(string)  # 添加信息进列表
        elif os.path.isdir(item):  # 目录
            string = item + '  目录  ' + \
                     os.path.abspath(item) + '  ' + \
                     time.ctime(os.path.getctime(item)) + '  ' + '\n'
            dirList.append(string)
        else:  # 其它类型，如链接文件
            string = item + '  其它  ' + os.path.abspath(item) + '  ' + time.ctime(
                os.path.getctime(item)) + '  ' + str(round(os.path.getsize(item) / 1024, 2)) + 'kb\n'
            otherList.append(string)
    # 为方便查看，这里按照目录，文件，其它文件的顺序写入
    for dir in dirList:  # 写入目录信息
        os.write(f, str.encode(dir))
    for file in fileList:  # 写入文件信息
        os.write(f, str.encode(file))
    for other in otherList:  # 写入其它文件信息
        os.write(f, str.encode(other))
    os.close(f)  # 关闭文件


# 调用函数，这里的路径可修改成自己得路径
storeFileDir('D:\\Python\\PythonCode\\book_project\\chaper9\\example')
