# insert_data_sqlite3.py
#!/usr/bin/env python3
import sqlite3

DB_Name = 'test.db'
# 连接数据库，如果不存在则会在当前目录创建
conn = sqlite3.connect(DB_Name)
try:
    # 创建游标
    cursor = conn.cursor()
    # 待插入的数据
    insertData = [('2016081111', '张三', '男', 18),
                  ('2016081112', '李四', '男', 20), ('2016081113', '王五', '男', 19)]
    # 插入一条数据的SQL语句
    INSERT_SQL = '''
            INSERT INTO STUDENT VALUES('2016081114','李丽','女',18);
            '''
    # 插入多条数据的SQL语句
    INSERT_MANY_SQL = '''
                INSERT INTO STUDENT VALUES('2016081115','吴芳','女',18),('2016081116','胡月','女',20);
                '''
    # 插入一条数据
    cursor.execute(INSERT_SQL)
    # 插入多条数据
    cursor.execute(INSERT_MANY_SQL)
    # 插入多条数据
    cursor.executemany('INSERT INTO STUDENT VALUES(?,?,?,?);', insertData)

    # 提交到数据库
    conn.commit()
    print('插入数据到表STUDENT成功')
except Exception as e:
    print(e)
    # 回滚
    conn.rollback()
    print('插入数据到表STUDENT失败')
finally:
    # 关闭数据库
    conn.close()
