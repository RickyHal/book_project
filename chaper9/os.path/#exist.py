# exist.py
import os

path = 'C:\\Users\\1\\test.txt'
if os.path.exists(path):  # 删除文件前先确认文件是否存在
    try:
        os.remove(path)
        print('删除成功！')
    except:
        print('删除失败！')
else:
    print('文件不存在！')
