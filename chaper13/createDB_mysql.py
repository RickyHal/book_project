# createDB_mysql.py
#!/usr/bin/env python3
import pymysql

# 连接数据库,地址：localhost,账号：root,密码：123
db = pymysql.connect('localhost', 'root', '123')

# 创建一个游标对象
cursor = db.cursor()

try:
    # 创建数据库TEST,默认编码为UTF-8
    cursor.execute(
        'CREATE SCHEMA TEST DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;')

    # 显示所有的数据库
    cursor.execute('SHOW DATABASES;')
    print(cursor.fetchall())
except Exception as e:
    # 创建失败
    print(e)
    db.rollback()
finally:
    # 关闭数据库连接
    cursor.close()
    db.close()
