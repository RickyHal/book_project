# sqlite3_init.py
#!/usr/bin/env python3
import sqlite3

# 创建表
CREATE_TABLE_SQL = '''
        CREATE TABLE STUDENT_INFO (
        SNO CHAR(10) NOT NULL,
        SNAME VARCHAR(20) NOT NULL,
        SAGE int NOT NULL,
        SSEX CHAR(1) NOT NULL,
        SACADEMY VARCHAR(20) NOT NULL,
        SGRADE int NOT NULL,
        SCLASS int NOT NULL,
        PRIMARY KEY(SNO))
      '''
# 添加数据
CREATE_DATA_SQL = '''
                     INSERT INTO STUDENT_INFO VALUES('2016081111','张三',20,'男','软件工程学院',2016,03),
                     ('2016061111','王杰',21,'男','网络工程学院',2016,03),('2016071113','周顺',19,'男','大气科学学院',2016,03),
                     ('2017081180','李伟',20,'男','软件工程学院',2017,02),('2016081201','王丽',20,'女','软件工程学院',2016,05)
                  '''

# 初始化


def init():
    try:
        DB_Name = 'students.db'
        # 连接数据库，如果不存在则会在当前目录创建
        conn = sqlite3.connect(DB_Name)
        # 创建游标
        cursor = conn.cursor()
        # 创建数据库表
        cursor.execute(CREATE_TABLE_SQL)
        # 插入数据
        cursor.execute(CREATE_DATA_SQL)
        conn.commit()
        print('初始化成功')
    except Exception as e:
        conn.rollback()
        print('初始化失败', e)
    finally:
        # 关闭数据库
        conn.close()


if __name__ == "__main__":
    init()
