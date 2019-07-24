# select_data_sqlite3.py
#!/usr/bin/env python3
import sqlite3

DB_Name = 'test.db'
# 连接数据库，如果不存在则会在当前目录创建
conn = sqlite3.connect(DB_Name)
try:
    # 创建游标
    cursor = conn.cursor()
    # 查询数据的SQL语句
    SQL = '''
          SELECT * FROM STUDENT;
          '''
    # 查询数据
    cursor.execute(SQL)

    # 获取一条数据
    one = cursor.fetchone()
    print(type(one))
    print(one)
    all = cursor.fetchall()
    print(type(all))
    # 获取所有数据
    for row in all:
        print(row)
except Exception as e:
    print(e)
    print('查询数据失败')
finally:
    # 关闭数据库
    conn.close()
