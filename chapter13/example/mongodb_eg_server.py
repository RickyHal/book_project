# mongodb_eg_server.py
#!/usr/bin/env python3
import socket
import requests
import json

host = 'http://openapi.tuling123.com/openapi/api/v2'
data = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": ""
        }
    },
    "userInfo": {
        "apiKey": "3344b5594def4c8980098100acbb6ab2",
        "userId": "123"
    }
}


def get_message(message):
    data['perception']['inputText']['text'] = message
    sendInfo = str(data).encode('utf-8')
    res = requests.post(host, data=sendInfo)
    res.encoding = 'utf-8'
    reply = json.loads(res.text)
    return reply['results'][0]['values']['text']


if __name__ == '__main__':
    server = socket.socket()
    server.bind((socket.gethostname(), 8888))
    print('hostname=%s,port=8888,开始监听...' % (socket.gethostname()))
    server.listen(5)
    conn, address = server.accept()
    while True:
        receive = conn.recv(1024).decode('utf-8')
        print('服务端收到：', receive)
        reply = get_message(receive)
        conn.send(reply.encode('utf-8'))
        print('服务端发送：', reply)
