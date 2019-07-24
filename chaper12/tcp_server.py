# tcp_server.py
#!/usr/bin/env python3
import socket
import time
try:
    s = socket.socket()
    hostname = socket.gethostname()
    # 绑定套接字地址
    s.bind((hostname, 8888))
    s.listen(5)
    print(time.strftime('%Y-%m-%d %H:%M:%S',
                        time.localtime(time.time())), '服务端准备完毕，等待客户端连接')
    con, address = s.accept()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
          '客户端已连接上服务端，连接地址：', address)
    message = '你好，我是服务端'
    # 发送消息，必须对发送的内容进行编码
    con.send(message.encode('utf-8'))
    print(time.strftime('%Y-%m-%d %H:%M:%S',
                        time.localtime(time.time())), '服务端发送：', message)
    # 关闭套接字
    con.close()
except Exception as e:
    print('建立TCP服务端失败', e)
