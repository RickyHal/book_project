# alter_table_mysql.py
#!/usr/bin/env python3
import pymysql

# 连接数据库,地址：localhost,账号：root,密码：123,数据库：test
db = pymysql.connect('localhost', 'root', '123', 'test')

# 创建一个游标对象
cursor = db.cursor()

try:
    # 新增列的SQL语句
    ADD_SQL = '''
        ALTER TABLE STUDENT ADD COLUMN SSEX VARCHAR(1) NOT NULL,ADD COLUMN SAGE INT NOT NULL;
      '''
    # 删除列的SQL语句
    DELETE_SQL = '''
             ALTER TABLE STUDENT DROP COLUMN SAGE
              '''
    # 新增列
    cursor.execute(ADD_SQL)
    # 删除列
    cursor.execute(DELETE_SQL)
    # 提交到数据库
    db.commit()
    print('修改成功')
except Exception as e:
    # 修改失败
    print('修改失败', e)
    db.rollback()
finally:
    # 关闭数据库连接
    cursor.close()
    db.close()
