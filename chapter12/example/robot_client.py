# robot_client.py
#!/usr/bin/env python3
import socket

try:
    s = socket.socket()
    hostname = socket.gethostname()
    s.connect((hostname, 8888))
    message = input('客户端：')
    while message:
        # 发送给服务端消息，必须对发送的消息进行编码
        s.send(message.encode('utf-8'))
        # 接收服务端消息并解码
        response = s.recv(1024).decode('utf-8')
        print('服务端：', response)
        message = input('客户端：')
    # 关闭套接字
    s.close()
except Exception as e:
    print('建立客户端失败', e)
