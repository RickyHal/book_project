# create_table_mysql.py
#!/usr/bin/env python3
import pymysql

# 连接数据库,地址：localhost,账号：root,密码：123,数据库：test
db = pymysql.connect('localhost', 'root', '123', 'test')

# 创建一个游标对象
cursor = db.cursor()

try:
    # 创建STUDENT表的SQL语句，默认编码为UTF-8
    SQL = '''
        CREATE TABLE STUDENT (
        SNO CHAR(10),
        SNAME VARCHAR(20) NOT NULL,
        PRIMARY KEY(SNO)
       ) DEFAULT CHARSET=utf8;
      '''
    cursor.execute(SQL)
    # 显示创建的表
    cursor.execute('SHOW TABLES;')
    print(cursor.fetchall())

except Exception as e:
    # 创建失败
    print(e)
    db.rollback()
finally:
    # 关闭数据库连接
    cursor.close()
    db.close()
