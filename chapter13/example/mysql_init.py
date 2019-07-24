# mysql_init.py
#!/usr/bin/env python3
import pymysql

# 创建模式
CREATE_SCHEMA_SQL = '''
                  CREATE SCHEMA BANK  CHARSET=utf8;
                  '''
# 创建表
CREATE_TABLE_SQL = '''
        CREATE TABLE ACCOUNT (
        ACCOUNT_ID VARCHAR(20) NOT NULL,
        ACCOUNT_PASSWD CHAR(6) NOT NULL,
        #DECIMAl为用于保存精确数字的类型，DECIMAL(10,2)表示总位数最大为12位，其中整数10位，小数2位
        MONEY DECIMAL(10,2) NOT NULL,
        PRIMARY KEY(ACCOUNT_ID)) DEFAULT CHARSET=utf8;
      '''
# 创建银行账户
CREATE_ACCOUNT_SQL = '''
                     INSERT INTO ACCOUNT VALUES('001','123456',100.00);
                     '''

# 初始化


def init():
    try:
        DB = pymysql.connect('localhost', 'root', '123')
        cursor1 = DB.cursor()
        cursor1.execute(CREATE_SCHEMA_SQL)
        DB = pymysql.connect('localhost', 'root', '123', 'bank')
        cursor2 = DB.cursor()
        cursor2.execute(CREATE_TABLE_SQL)
        cursor2.execute(CREATE_ACCOUNT_SQL)
        DB.commit()
        print('初始化成功')
    except Exception as e:
        print('初始化失败', e)
    finally:
        cursor1.close()
        cursor2.close()
        DB.close()


if __name__ == "__main__":
    init()
