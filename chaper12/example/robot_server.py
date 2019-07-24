# robot_server.py
#!/usr/bin/env python3
import socket

try:
    s = socket.socket()
    hostname = socket.gethostname()
    # 绑定套接字地址
    s.bind((hostname, 8888))
    s.listen(5)
    print('服务端准备完毕，等待客户端连接')
    con, address = s.accept()
    print('客户端已连接上服务端，连接地址：', address)
    while True:
        # 接收客户端消息并解码
        message = con.recv(1024).decode('utf-8')
        print('服务端接收：', message)
        if message:
            # 构造回复给客户端的消息
            reply = (message.replace('你', '我').replace('不', '').replace(
                '吗', '').replace('？', '！').replace('?', '!'))
            # 发送消息，必须对发送的内容进行编码
            con.send(reply.encode('utf-8'))
            print('服务端发送：', reply)
        else:
            print('客户端不再发送消息')
            break
except Exception as e:
    print('建立服务端失败', e)
finally:
    # 关闭套接字
    con.close()
    s.close()
