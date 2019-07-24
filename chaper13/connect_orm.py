# connect_orm.py
#!/usr/bin/env python3
from sqlalchemy import create_engine

try:
    # 连接MySQL数据库，地址：localhost:3306,账号：root,密码：123,数据库：test
    MySQLEngine = create_engine(
        'mysql+pymysql://root:123@localhost:3306/test?charset=utf8', encoding='utf-8')
    print('连接MySQL数据库成功', MySQLEngine)
    # 连接SQLite数据库，如果当前目录不存在test.db文件则会自动生成
    SQLiteEngine = create_engine('sqlite:///:test.db', encoding='utf-8')
    print('连接SQLite数据库成功', SQLiteEngine)
except Exception as e:
    print('连接数据库失败', e)
