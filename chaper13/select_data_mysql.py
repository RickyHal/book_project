# select_data_mysql.py
#!/usr/bin/env python3
import pymysql

# 连接数据库,地址：localhost,账号：root,密码：123,数据库：test,
# 编码UTF-8
db = pymysql.connect('localhost', 'root', '123', 'test', charset='utf8')

# 创建一个游标对象
cursor = db.cursor()

# SQL语句
SQL = '''
      SELECT * FROM STUDENT;
      '''
try:
    # 查询所有的数据
    cursor.execute(SQL)
    # 查询到的条数
    print('查询到了%s条数据' % (cursor.rowcount))
    # 获取一条数据
    one = cursor.fetchone()
    print(type(one))
    print(one)
    # 获取所有数据
    for item in cursor.fetchall():
        print(item)
except Exception as e:
    # 插入失败
    print('查询失败', e)
finally:
    # 关闭数据库连接
    cursor.close()
    db.close()
