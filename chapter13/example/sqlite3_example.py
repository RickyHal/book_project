# sqlite3_example.py
#!/usr/bin/env python3
import sqlite3

# 数据库连接
CONN = None
# 数据库文件名
DB_NAME = 'students.db'


# 学生类
class STUDENT(object):

    def __init__(self):
        super(STUDENT, self).__init__()

    # 打印查询出的数据
    def print_data(self, data):
        print('查询到%s条数据\n学号\t姓名\t年龄\t性别\t学院\t年级\t班级' % (len(data)))
        for row in data:
            print('%s\t%s\t%s\t%s\t%s\t%s\t%s' % (row))

    # 查询所有数据
    def query_data(self, *by_key):
        cursor = CONN.cursor()
        if by_key:
            SQL = self.concat_sql(by_key[0], by_key[1])
        else:
            SQL = 'SELECT * FROM STUDENT_INFO'
        print('EXECUTE SQL:%s' % (SQL))
        try:
            data = cursor.execute(SQL).fetchall()
            if len(data) > 0:
                self.print_data(data)
            else:
                print('没有查询到数据')
                return 'no data'
        except Exception as e:
            print('查询数据失败', e)
        finally:
            cursor.close()

    # 构造SQL语句
    def concat_sql(self, by, key):
        SQL = 'SELECT * FROM STUDENT_INFO WHERE '
        if by == 'sno':
            SQL = SQL + "SNO = " + key
        elif by == 'sname':
            SQL = SQL + "SNAME LIKE '%" + key + "%'"
        elif by == 'sacademy':
            SQL = SQL + "SACADEMY LIKE '%" + key + "%'"
        return SQL

    # 添加学生信息
    def add_data(self, insert_data):
        cursor = CONN.cursor()
        SQL = "INSERT INTO STUDENT_INFO VALUES('%s','%s','%s','%s','%s','%s','%s')" % (insert_data[
            0], insert_data[1], insert_data[2], insert_data[3], insert_data[4], insert_data[5], insert_data[6])
        print('EXECUTE SQL:%s' % (SQL))
        try:
            cursor.execute(SQL)
            CONN.commit()
            print('添加数据成功')
        except Exception as e:
            CONN.rollback()
            print('添加数据失败', e)
        finally:
            cursor.close()

    # 更新学生信息
    def update_data(self, sno, update_data):
        cursor = CONN.cursor()
        SQL = "UPDATE STUDENT_INFO SET SNO='%s',SNAME='%s',SAGE='%s',SSEX='%s',SACADEMY='%s',SGRADE='%s',SCLASS='%s' WHERE SNO='%s'" % (update_data[0], update_data[1], update_data[2], update_data[3],
                                                                                                                                        update_data[4], update_data[5], update_data[6], sno)
        print('EXECUTE SQL:%s' % (SQL))
        try:
            cursor.execute(SQL)
            CONN.commit()
            print('更新数据成功')
        except Exception as e:
            CONN.rollback()
            print('更新数据失败', e)
        finally:
            cursor.close()

    # 删除学生信息
    def delete_data(self, sno):
        cursor = CONN.cursor()
        SQL = 'DELETE FROM STUDENT_INFO WHERE SNO =%s' % (sno)
        print('EXECUTE SQL:%s' % (SQL))
        try:
            cursor.execute(SQL)
            CONN.commit()
            print('删除数据成功')
        except Exception as e:
            CONN.rollback()
            print('删除数据失败', e)
        finally:
            cursor.close()

# 打印菜单


def menu():
    print('\n***************\n请选择您的操作：')
    print('1.查询所有学生的信息')
    print('2.按学号查询学生的信息')
    print('3.按姓名查询学生的信息')
    print('4.按学院查询学生的信息')
    print('5.添加学生信息')
    print('6.修改学生信息')
    print('7.删除学生信息')
    print('8.退出')
    return input()

# 主函数


def main():
    global CONN, DB_NAME
    # 连接数据库
    CONN = sqlite3.connect(DB_NAME)
    student = STUDENT()
    choose = menu()
    while choose != '8':
        if choose == '1':
            student.query_data()
        elif choose == '2':
            sno = input('请输入学号：')
            student.query_data('sno', sno)
        elif choose == '3':
            sname = input('请输入姓名：')
            student.query_data('sname', sname)
        elif choose == '4':
            sacademy = input('请输入学院：')
            student.query_data('sacademy', sacademy)
        elif choose == '5':
            insert_data = input(
                '请输入添加的学生的信息，数据之间以空格分开：\n学号\t姓名\t年龄\t性别\t学院\t年级\t班级\n').split(' ')
            if len(insert_data) != 7:
                print('数据不完整')
            else:
                student.add_data(insert_data)
        elif choose == '6':
            sno = input('请输入修改的学生的学号：')
            if student.query_data('sno', sno) == 'no data':
                print('学生不存在')
            else:
                update_data = input(
                    '请输入修改的学生的信息，数据之间以空格分开：\n学号\t姓名\t年龄\t性别\t学院\t年级\t班级\n').split(' ')
                if len(update_data) != 7:
                    print('数据不完整')
                else:
                    student.update_data(sno, update_data)
        elif choose == '7':
            sno = input('请输入删除的学生的学号：')
            if student.query_data('sno', sno) == 'no data':
                print('学生不存在')
            else:
                student.delete_data(sno)
        choose = menu()
    print('感谢您的使用')
    CONN.close()


if __name__ == "__main__":
    main()
