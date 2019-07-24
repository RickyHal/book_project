# mysql_example.py
#!/usr/bin/env python3
import decimal
import pymysql

# 全局变量，数据库连接
DB = None

# 银行账号类


class Account(object):

    def __init__(self, account_id, account_passwd):
        super(Account, self).__init__()
        # 账号
        self.account_id = account_id
        # 密码
        self.account_passwd = account_passwd

    # 登录检查
    def check_account(self):
        cursor = DB.cursor()
        try:
            sql = "select * from account where account_id=%s and account_passwd=%s" % (
                self.account_id, self.account_passwd)
            cursor.execute(sql)
            if cursor.fetchall():
                return True
            else:
                return 0.00
        except Exception as e:
            print("系统错误", e)
        finally:
            cursor.close()

    # 查询余额
    def query_money(self):
        cursor = DB.cursor()
        try:
            sql = "select money from account where account_id=%s and account_passwd=%s" % (
                self.account_id, self.account_passwd)
            cursor.execute(sql)
            money = cursor.fetchone()[0]
            if money:
                return str(money.quantize(decimal.Decimal('0.00')))
            else:
                return '0.00'
        except Exception as e:
            print("系统错误", e)
        finally:
            cursor.close()

    # 取钱
    def reduce_money(self, money):
        cursor = DB.cursor()
        try:
            has_money = self.query_money()
            # 检查余额是否充足
            if decimal.Decimal(has_money) >= decimal.Decimal(money):
                sql = "update account set money=money-%s where account_id=%s and account_passwd=%s" % (
                    money, self.account_id, self.account_passwd)
                cursor.execute(sql)
                if cursor.rowcount == 1:
                    DB.commit()
                    return True
                else:
                    DB.rollback()
                    return False
            else:
                print('余额不足')
        except Exception as e:
            DB.rollback()
            print("系统错误", e)
        finally:
            cursor.close()

    # 存钱
    def add_money(self, money):
        cursor = DB.cursor()
        try:
            sql = "update account set money=money+%s where account_id=%s and account_passwd=%s" % (
                money, self.account_id, self.account_passwd)
            cursor.execute(sql)
            if cursor.rowcount == 1:
                DB.commit()
                return True
            else:
                DB.rollback()
                return False
        except Exception as e:
            DB.rollback()
            print("系统错误", e)
        finally:
            cursor.close()


def main():
    global DB
    # 连接数据库
    DB = pymysql.connect('localhost', 'root', '123', 'bank')
    # 登录
    from_account_id = input('欢迎使用，请输入您的账号：')
    from_account_passwd = input('密码：')
    account = Account(from_account_id, from_account_passwd)
    if account.check_account():
        # 登录成功
        choose = input(
            '\n******************\n登录成功，请选择您的操作：\n1.查询余额\n2.取钱\n3.存钱\n4.取卡\n')
        while choose != '4':
            if choose == '1':
                print('您的账户的余额为%s元' % (account.query_money()))
            elif choose == '2':
                money = input('您的余额为:%s元\n请输入您取钱的金额：' %
                              (account.query_money()))
                if account.reduce_money(money):
                    print('取钱成功，您的余额还有%s元,请按任意键继续' % (account.query_money()))
                else:
                    print('取钱失败，请按任意键继续')
            elif choose == '3':
                money = input('请输入您存钱的金额：')
                if account.add_money(money):
                    print('存钱成功，您的余额还有%s元,请按任意键继续\n' % (account.query_money()))
                else:
                    print('存钱失败，请按任意键继续')
            choose = input(
                '\n******************\n请选择您的操作：\n1.查询余额\n2.取钱\n3.存钱\n4.取卡\n')
    else:
        print('登录失败，账号或密码错误')
    print('感谢您的使用')
    DB.close()


if __name__ == "__main__":
    main()
