# connect_mysql.py
#!/usr/bin/env python3
import pymysql

# 连接数据库,地址：localhost,账号：root,密码：123
db = pymysql.connect('localhost', 'root', '123')

# 创建一个游标对象
cursor = db.cursor()

# 执行SQL语句
cursor.execute('SHOW DATABASES;')

# 获取一条数据
one = cursor.fetchone()
print(one)

# 获取剩余的所有数据
all = cursor.fetchall()
print(all)
print('所有的数据库：')
print(one[0])
for row in all:
    print(row[0])

# 关闭数据库连接
cursor.close()
db.close()
