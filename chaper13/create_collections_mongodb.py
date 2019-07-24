# create_collections_mongodb.py
#!/usr/bin/env python3
import pymongo

try:
    # 连接MongoDB数据库，地址：localhost:27017，账号：test，密码：123
    client = pymongo.MongoClient("mongodb://localhost:27017/test:123")
    # 显示所有的数据库
    print('所有的数据库：', client.list_database_names())
    # 连接创建test数据库,真正插入文档后才会创建
    db = client['test']
    # 显示所有的数据库
    print('所有的数据库：', client.list_database_names())
    # 连接创建test数据库下的student集合，插入文档后才会创建
    mycol = db['student']
    # 显示所有的集合
    print('所有的集合：', db.list_collection_names())
except Exception as e:
    print('创建集合失败', e)
