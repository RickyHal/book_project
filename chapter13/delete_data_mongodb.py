# delete_data_mongodb.py
#!/usr/bin/env python3
import pymongo

try:
    # 连接MongoDB数据库，地址：localhost:27017，账号：test，密码：123
    client = pymongo.MongoClient("mongodb://localhost:27017/test:123")
    # 连接创建test数据库,真正插入文档后才会创建
    db = client['test']
    # 连接test数据库下的student集合
    mycol = db['student']

    # 显示所有的集合
    print('所有的集合：', db.list_collection_names())
    # 查询所有数据
    print('删除文档前：')
    for row in mycol.find():
        print(row)

    # 删除学号为2016081111的文档
    mycol.delete_one({'sno': '2016081111'})
    # 删除学号以2016开头的文档
    res = mycol.delete_many({'sno': {'$regex': '^2016'}})
    print('删除了%s条文档' % (res.deleted_count))
    # 删除所有的文档
    mycol.delete_many({})
    # 查询所有文档
    print('删除文档后：')
    for row in mycol.find():
        print(row)

    # 删除student集合
    mycol.drop()
    # 显示所有的集合
    print('所有的集合：', db.list_collection_names())
except Exception as e:
    print('删除文档失败', e)
