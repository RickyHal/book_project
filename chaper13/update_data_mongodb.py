# update_data_mongodb.py
#!/usr/bin/env python3
import pymongo

try:
    # 连接MongoDB数据库，地址：localhost:27017，账号：test，密码：123
    client = pymongo.MongoClient("mongodb://localhost:27017/test:123")
    # 连接创建test数据库,真正插入文档后才会创建
    db = client['test']
    # 连接test数据库下的student集合
    mycol = db['student']

    # 修改前
    print('文档更新前：', [info for info in mycol.find({'sno': '2016081111'})])
    # 修改学号为2016081111的学生的姓名为李华
    mycol.update_one({'sno': '2016081111'}, {'$set': {'name': '李华'}})
    # 修改后
    print('文档修改后：', [info for info in mycol.find({'sno': '2016081111'})])

    # 为学号尾号为3的学生新增属性ssex
    mycol.update_many({'sno': {'$regex': '3$'}}, {'$set': {'ssex': '男'}})
    res = mycol.find({'sno': {'$regex': '3$'}})
    # 打印查询结果
    print('学号结尾为3的学生：')
    for row in res:
        print(row)
except Exception as e:
    print('更新文档失败', e)
