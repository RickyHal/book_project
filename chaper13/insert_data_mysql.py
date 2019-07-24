# insert_data_mysql.py
#!/usr/bin/env python3
import pymysql

# 连接数据库,地址：localhost,账号：root,密码：123,数据库：test,
# 编码：UTF-8
db = pymysql.connect('localhost', 'root', '123', 'test', charset='utf8')

# 创建一个游标对象
cursor = db.cursor()

# 待插入的数据
insertData = [('2016081111', '张三', '男'),
              ('2016081112', '李四', '男'), ('2016081113', '王五', '男')]
# 插入一条数据的SQL语句
INSERT_SQL = '''
            INSERT INTO STUDENT VALUES('2016081114','李丽','女');
            '''
# 插入多条数据的SQL语句
INSERT_MANY_SQL = '''
                INSERT INTO STUDENT VALUES('2016081115','吴芳','女'),('2016081116','胡月','女');
                '''
try:
    # 插入一条数据
    cursor.execute(INSERT_SQL)
    # 插入多条数据
    cursor.execute(INSERT_MANY_SQL)
    # 插入多条数据
    cursor.executemany('INSERT INTO STUDENT VALUES(%s,%s,%s);', insertData)
    # 提交到数据库
    db.commit()
    print('插入成功')
except Exception as e:
    # 插入失败
    db.rollback()
    print('插入失败', e)

# 关闭数据库连接
cursor.close()
db.close()
