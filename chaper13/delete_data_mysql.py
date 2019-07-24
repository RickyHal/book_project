# delete_data_mysql.py
#!/usr/bin/env python3
import pymysql

# 连接数据库,地址：localhost,账号：root,密码：123,数据库：test
db = pymysql.connect('localhost', 'root', '123', 'test', charset='utf8')

# 创建一个游标对象
cursor = db.cursor()

SNO = '2016081111'
# 删除数据SQL语句
DELETE_SQL = '''
      DELETE FROM STUDENT WHERE SNO='%s';
      ''' % (SNO)
# 查询数据SQL语句
SELECT_SQL = '''
            SELECT * FROM STUDENT WHERE SNO='%s'
           ''' % (SNO)
try:
    # 删除数据前
    cursor.execute(SELECT_SQL)
    print('删除前:', cursor.fetchall())
    # 删除数据
    cursor.execute(DELETE_SQL)
    # 提交到数据库
    db.commit()
    # 删除数据后
    cursor.execute(SELECT_SQL)
    print('删除后:', cursor.fetchall())
except Exception as e:
    # 删除失败，回滚
    db.rollback()
    print('删除失败')
finally:
    # 关闭数据库连接
    cursor.close()
    db.close()
