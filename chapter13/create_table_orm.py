# create_table_orm.py
#!/usr/bin/env python3
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建基类
BASE = declarative_base()

# 定义学生对象


class Student(BASE):
    # 表的名字:STUDENT
    __tablename__ = 'STUDENT'
    # 学号
    sno = Column(String(10))
    # 姓名
    sname = Column(String(20), primary_key=True)
    # 创建表的参数
    __table_args__ = {
        "mysql_charset": "utf8"
    }


try:
    # 连接MySQL数据库,地址：localhost:3306,账号：root,密码：123,数据库：test
    MySQLEngine = create_engine(
        'mysql+pymysql://root:123@localhost:3306/test?charset=utf8')
    # 创建STUDENT表
    BASE.metadata.create_all(MySQLEngine)
    print('创建STUDENT表成功')
except Exception as e:
    print("连接SQLite数据库失败", e)
