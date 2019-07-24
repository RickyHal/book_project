# insert_data_mongodb.py
#!/usr/bin/env python3
import pymongo

try:
    # 连接MongoDB数据库，地址：localhost:27017，账号：test，密码：123
    client = pymongo.MongoClient("mongodb://localhost:27017/test:123")
    # 连接创建test数据库,真正插入文档后才会创建
    db = client['test']
    # 连接创建student集合，插入文档后才会创建成功
    mycol = db['student']
    # 显示所有的集合
    print('所有的集合：', db.list_collection_names())
    # 待插入的文档
    insertData = [
        {'name': '张三', 'sno': '2016081111'},
        {'name': '李四', 'sno': '2016081112'},
        {'name': '王五', 'sno': '2016081113'}
    ]

    # 插入一条文档
    res = mycol.insert_one({'name': '李丽', 'sno': '2016081114'})
    print('插入一条文档返回InsertOneResult对象：', res)

    # 插入多条文档
    res = mycol.insert_many(insertData)
    print('插入多条文档返回InsertManyResult对象：', res)

    # 插入指定_id的文档
    res = mycol.insert({'_id': '1', 'name': '张伟', 'sno': '2017081113'})
    print('插入指定_id的文档返回指定的_id：', res)

    # 显示所有的集合
    print(db.list_collection_names())

    # 插入重复_id的文档,会报错
    res = mycol.insert_one({'_id': '1', 'name': '张伟', 'sno': '2016081113'})
    print('插入重复的_id：', res)
except Exception as e:
    print('插入文档失败', e)
