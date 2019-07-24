# db_manage_mysql.py
#!/usr/bin/env python3
import pymysql

# 连接数据库,地址：localhost,账号：root,密码：123
db = pymysql.connect('localhost', 'root', '123')

# 创建一个游标对象
cursor = db.cursor()

try:
    # 创建数据库
    cursor.execute('CREATE SCHEMA TEST DEFAULT CHARSET=utf8;')

    # 显示所有的数据库
    cursor.execute('SHOW DATABASES;')
    print(cursor.fetchall())

    # 删除数据库
    cursor.execute('DROP SCHEMA TEST;')

    # 显示所有的数据库
    cursor.execute('SHOW DATABASES;')
    print(cursor.fetchall())
except Exception as e:
    print(e)
    db.rollback()
finally:
    # 关闭数据库连接
    cursor.close()
    db.close()
