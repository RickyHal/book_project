# alter_table_sqlite3.py
#!/usr/bin/env python3
import sqlite3

DB_Name = 'test.db'
# 连接数据库，如果不存在则会在当前目录创建
conn = sqlite3.connect(DB_Name)
try:
    # 创建一个游标对象
    cursor = conn.cursor()
    # 新增列的SQL语句
    ADD_SQL1 = '''
        ALTER TABLE STUDENT ADD COLUMN SSEX VARCHAR(1);
        '''
    ADD_SQL2 = '''
        ALTER TABLE STUDENT ADD COLUMN SAGE INT;
        '''
    # 新增列
    cursor.execute(ADD_SQL1)
    cursor.execute(ADD_SQL2)
    # 提交到数据库
    conn.commit()
    print('修改成功')
except Exception as e:
    print('修改失败', e)
    # 回滚
    conn.rollback()
finally:
    # 关闭数据库
    conn.close()
