# select_data_mongodb.py
#!/usr/bin/env python3
import pymongo

try:
    # 连接MongoDB数据库，地址：localhost:27017，账号：test，密码：123
    client = pymongo.MongoClient("mongodb://localhost:27017/test:123")
    # 连接创建test数据库,真正插入文档后才会创建
    db = client['test']
    # 连接test数据库下的student集合
    mycol = db['student']

    # 查询所有文档
    res = mycol.find()
    # 打印查询结果
    print('查询结果：', res)
    print('查询结果的类型：', type(res))
    print('student集合所有的文档：')
    for row in res:
        print(row)

    # 查询学号为2016081111的学生信息
    res = mycol.find({'sno': '2016081111'})
    # 打印查询结果
    print('学号为2016081111的学生：', [info for info in res])
    # 查询学号以1结尾的学生信息
    res = mycol.find({'sno': {'$regex': '3$'}})
    # 打印查询结果
    print('学号结尾为3的学生：')
    for row in res:
        print(row)
except Exception as e:
    print('查询文档失败', e)
