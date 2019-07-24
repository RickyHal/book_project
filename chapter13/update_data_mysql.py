# update_data_mysql.py
#!/usr/bin/env python3
import pymysql

# 连接数据库,地址：localhost,账号：root,密码：123,数据库：test
db = pymysql.connect('localhost', 'root', '123', 'test', charset='utf8')

# 创建一个游标对象
cursor = db.cursor()

SNAME = '李华'
# 更新数据SQL语句
UPDATE_SQL = '''
      UPDATE STUDENT SET SNAME='%s' WHERE SNO='2016081111';
      ''' % (SNAME)
# 查询数据SQL语句
SELECT_SQL = '''
            SELECT * FROM STUDENT WHERE SNO='%s'
           ''' % ('2016081111')
try:
    # 更新数据前
    cursor.execute(SELECT_SQL)
    print('更新前:', cursor.fetchall())
    # 更新数据
    cursor.execute(UPDATE_SQL)
    # 提交到数据库
    db.commit()
    # 更新数据后
    cursor.execute(SELECT_SQL)
    print('更新后:', cursor.fetchall())
except Exception as e:
    # 更新失败,回滚
    db.rollback()
    print('更新失败', e)
finally:
    # 关闭数据库连接
    cursor.close()
    db.close()
