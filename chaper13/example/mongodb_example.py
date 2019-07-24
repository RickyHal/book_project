# mongodb_example.py
#!/usr/bin/env python3
import os
import time
import pymongo
import socket
import requests
import json
import threading

# 连接MongoDB数据库，地址：localhost:27017，账号：test，密码：123
CLIENT = pymongo.MongoClient("mongodb://localhost:27017/test:123")


# 服务端
class Server(threading.Thread):
    # 图灵机器人API
    __host = 'http://openapi.tuling123.com/openapi/api/v2'
    # 图灵机器人请求数据
    __data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": ""  # 消息内容
            }
        },
        "userInfo": {
            "apiKey": "申请的API KEY",
            "userId": "123"
        }
    }

    def __init__(self):
        super(Server, self).__init__()

    def run(self):
        # 创建socket对象
        server = socket.socket()
        # 绑定地址和端口
        server.bind((socket.gethostname(), 8888))
        server.listen(5)
        conn, address = server.accept()
        while True:
            # 接收客户端消息
            receive = conn.recv(1024).decode('utf-8')
            # 请求图灵机器人API，获取回复给客户端的内容
            reply = self.get_message(receive)
            # 保存聊天记录
            self.save_message(reply, receive)
            # 回复客户端消息
            conn.send(reply.encode('utf-8'))

    def get_message(self, message):
        try:
            # 设置消息内容
            self.__data['perception']['inputText']['text'] = message
            sendInfo = str(self.__data).encode('utf-8')
            # 将__data使用post的方式发送到__host,请求图灵机器人的回复
            res = requests.post(self.__host, data=sendInfo)
            res.encoding = 'utf-8'
            reply = json.loads(res.text)
            # 返回图灵机器人的回复
            return reply['results'][0]['values']['text']
        except:
            return '系统错误'

    # 保存聊天记录到MongoDB数据库
    def save_message(self, send, receive):
        try:
            records = [{'client': {'text': receive, 'time': time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}, 'server': {'text': send, 'time': time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}}]
            db = CLIENT['chatroom']
            mycol = db['record']
            mycol.insert_many(records)
        except:
            return '存储聊天记录失败'


# 客户端
class Client(threading.Thread):

    def __init__(self):
        super(Client, self).__init__()

    def run(self):
        message = input('您：')
        client = socket.socket()
        # 连接服务端
        client.connect((socket.gethostname(), 8888))
        while message != 'bye':
            # 发送消息
            client.send(message.encode('utf-8'))
            # 接收消息
            print('机器人:', client.recv(1024).decode('utf-8'))
            message = input('您：')
        client.close()
        os._exit(0)


if __name__ == '__main__':
    # 创建服务端线程和客户端线程
    server = Server()
    client = Client()
    server.start()
    client.start()
