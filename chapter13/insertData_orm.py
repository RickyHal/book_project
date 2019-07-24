# insert_data_orm.py
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
    # 连接MySQL数据库
    MySQLEngine = create_engine(
        'mysql+pymysql://root:123@localhost:3306/test?charset=utf8', encoding='utf-8')
    # 创建MySQL类型
    MySQLSession = sessionmaker(bind=MySQLEngine)
    # 创建session对象
    session = MySQLSession()

    # 使用ORM插入数据
    # 创建Student对象
    Stu = Student(sname='张三', sno='2016081111')
    # 将创建的对象添加进session中
    session.add(Stu)

    # 使用原生SQL插入数据
    session.execute(
        "INSERT INTO STUDENT VALUES('2016081115','吴芳'),('2016081116','胡月')")
    # 提交到数据库
    session.commit()
    # 关闭session
    session.close()
    print('插入数据成功')
except Exception as e:
    print("连接SQLite数据库失败", e)
