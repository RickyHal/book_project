# update_data_orm.py
#!/usr/bin/env python3
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建基类
BASE = declarative_base()

# 定义学生对象


class Student(BASE):
    # 表的名字:
    __tablename__ = 'STUDENT'

    sname = Column(String(20), primary_key=True)
    sno = Column(String(10))

    def __str__(self):  # 格式输出查询出的数据
        return '%s,%s' % (self.sname, self.sno)


try:
    # 连接MySQL数据库
    MySQLEngine = create_engine(
        'mysql+pymysql://root:123@localhost:3306/test?charset=utf8', encoding='utf-8')
    # 创建MySQL类型
    MySQLSession = sessionmaker(bind=MySQLEngine)
    # 创建session对象
    session = MySQLSession()
    # 查询学号为2016081111的学生
    Stu = session.query(Student).filter(Student.sno == '2016081111').first()
    print('更改前：', Stu)
    # 更改姓名为李华
    Stu.sname = '李华'
    # 提交到数据库
    session.commit()
    print('更改后：', Stu)
    # 关闭session
    session.close()
except Exception as e:
    print("连接SQLite数据库失败", e)
