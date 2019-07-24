# example2.py
import os
import sys
import time  # 引入time模块将返回的浮点型秒数转换成易于查看的时间
import shutil  # 用于删除非空文件夹

'''
function:获取路径path下的所有文件和目录的名称
parameter：
  1.path:路径
return：None
'''


def getFileDir(path):
    # 声明全局变量
    global fileList
    global dirList
    global otherList
    os.chdir(path)  # 更改当前目工作目录
    # 遍历当前路径文件和目录
    for item in os.listdir():
        if os.path.isfile(item):  # 文件
            fileList.append(item)  # 添加文件名进列表
        elif os.path.isdir(item):  # 目录
            dirList.append(item)
        else:  # 其它类型，如链接文件
            otherList.append(item)


'''
function:打印路径path下的所有文件和目录信息
parameter：
  1.path:路径
return：None
'''


def printFileDir(path):
    # 声明全局变量
    global fileList
    global dirList
    global otherList
    # 为方便查看，这里按照目录，文件，其它文件的顺序输出结果
    print('路径' + os.path.abspath(path) +
          '下的所有文件和目录信息：\n名称  类型  绝对路径  创建时间  文件大小  ')
    for dir in dirList:  # 输出目录信息
        print(dir + '  目录  ' +
              os.path.abspath(dir) + '  ' +
              time.ctime(os.path.getctime(dir)) + '  ' + '\n', end='')
    for file in fileList:  # 输出文件信息
        # 这里的文件大小单位转换成了kb类型的，并使用了round函数保留了两位小数
        print(file + '  文件  ' + os.path.abspath(file) + '  ' + time.ctime(
            os.path.getctime(file)) + '  ' + str(round(os.path.getsize(file) / 1024, 2)) + 'kb\n', end='')
    for other in otherList:  # 输出其它文件信息
        print(other + '  其它  ' + os.path.abspath(other) + '  ' + time.ctime(
            os.path.getctime(otherother)) + '  ' + str(round(os.path.getsize(other) / 1024, 2)) + 'kb\n')


'''
function:创建文件
parameter：
  1.fileName:文件名
return：
  1.bool:True创建成功，False创建失败
'''


def createFile(fileName):
    try:
        f = os.open(fileName, os.O_CREAT)
        os.close(f)
        return True
    except:
        return False


'''
function:创建目录
parameter：
  1.dirName:目录名
return：
  1.bool:True创建成功，False创建失败
'''


def createDir(dirName):
    try:
        os.mkdir(dirName)
        return True
    except:
        return False


'''
function:删除文件或目录
parameter：
  1.path:文件名或目录名
return：
  1.bool:True删除成功，False删除失败
'''


def deleteFileDir(path):
    try:
        global dirList  # 声明全局变量
        if path not in dirList:  # 删除文件
            os.remove(path)
            return True
        else:  # 删除目录
            shutil.rmtree(path)
            return True
    except:
        return False


'''
function:重命名或移动文件或目录
parameter：
  1.path:文件名或目录名
  2.newPath:新路径或新文件名或新目录名
return：
  1.bool:True重命名成功，False重命名失败
'''


def renameFileDir(path, newPath):
    try:
        os.rename(path, newPath)
        return True
    except:
        return False


'''
function:清空文件，目录，其他文件列表
parameter：None
return：None
'''


def clearList():
    # 声明全局变量
    global fileList
    global dirList
    global otherList
    fileList.clear()
    dirList.clear()
    otherList.clear()


'''
function:打印菜单和调用函数处理相应的操作
parameter：None
return：
  1.bool:True继续，False结束
'''


def menu():
    # 声明全局变量
    global path
    # 清空文件，目录，其他文件列表
    clearList()
    # 判断当前系统，进行清屏
    if os.name == 'nt':  # Windows系统
        os.system('cls')  # 清屏
    elif os.name == 'posix':  # Linux系统
        os.system('clear')
    # 获取当前路径文件，目录，其他文件名称
    getFileDir(path)
    # 输出当前路径文件和目录信息
    printFileDir(path)
    # 输入操作选项
    operation = input(
        '请输入要进行的操作编号：\n1.创建文件  2.创建目录  3.删除文件或目录  4.重命名文件或目录  5.移动文件或目录  6.重新输入路径  7.退出\n')
    # 创建文件
    if operation == '1':
        fileName = input('当前进行的操作：创建文件\n请输入创建的文件名：')
        if createFile(fileName):
            print('创建文件' + fileName + '成功！')
        else:
            print('创建文件' + fileName + '失败！')
    # 创建目录
    elif operation == '2':
        dirName = input('当前进行的操作：创建目录\n请输入创建的目录名：')
        if createDir(dirName):
            print('创建目录' + dirName + '成功！')
        else:
            print('创建目录' + dirName + '失败！')
    # 删除文件或目录
    elif operation == '3':
        deletePath = input('当前进行的操作：删除文件或目录\n请输入要删除文件名或目录名：')
        if deletePath in fileList or deletePath in dirList or deletePath in otherList:
            if deleteFileDir(deletePath):
                print('删除成功！')
            else:
                print('删除失败！')
        elif os.path.exists(deletePath) == False:
            print('文件或目录' + deletePath + '不存在！')
    # 重命名文件或目录
    elif operation == '4':
        renamePath = input('当前进行的操作：重命名文件或目录\n请输入要重命名的文件名或目录名：')
        if renamePath in fileList or renamePath in dirList or renamePath in otherList:
            newPath = input('请输入新名称：')
            if renameFileDir(renamePath, newPath):
                print('重命名成功！旧名称为：' + renamePath + '新名称为：' + newPath)
            else:
                print('重命名失败！')
        elif os.path.exists(renamePath) == False:
            print('文件或目录' + renamePath + '不存在！')
    # 移动文件或目录
    elif operation == '5':
        movePath = input('当前进行的操作：移动文件或目录\n请输入要移动的文件名或目录名：')
        if movePath in fileList or movePath in dirList or movePath in otherList:
            newPath = input('请输入该文件或目录的移动目标位置：')
            if renameFileDir(movePath, os.path.join(newPath, movePath)):
                print('移动成功！\n旧位置为：' + os.path.abspath(movePath) +
                      '\n新位置为：' + os.path.abspath(newPath) + os.sep + movePath)
            else:
                print('移动失败！')
        elif os.path.exists(movePath) == False:
            print('文件或目录' + movePath + '不存在！')
    # 重新输入路径
    elif operation == '6':
        try:
            newPath = input('请输入路径:')
            if os.path.isabs(path):
                path = os.path.normpath(newPath)
            else:
                input('路径不正确！按任意键回到主菜单')
        except:
            input('路径不正确！按任意键回到主菜单')
    # 退出，结束程序
    elif operation == '7':
        return False
    else:
        print('输入错误，请重新选择')
    # 接收任意键
    input('按任意键回到主菜单')
    return True


# 开始运行程序
if __name__ == '__main__':
    fileList = []  # 存储文件信息的列表
    dirList = []  # 存储目录信息的列表
    otherList = []  # 存储其它文件信息的列表
    path = ''  # 当前路径
    try:
        # 输入路径
        path = input('请输入路径:')
        if os.path.isabs(path):
            # 将路径转化为Python可使用的路径
            path = os.path.normpath(path)
            print(path)
        else:
            print('路径不正确！')
            sys.exit(0)  # 结束程序
    except:
        sys.exit(0)  # 结束程序
    while True:
        if menu() == False:
            break
    print('程序运行结束')
