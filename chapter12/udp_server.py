# udp_server.py
#!/usr/bin/env python3
import socket
import time

try:
    # 使用UDP协议
    s = socket.socket(type=socket.SOCK_DGRAM)
    hostname = socket.gethostname()
    # 绑定套接字地址
    s.bind((hostname, 8888))
    print(time.strftime('%Y-%m-%d %H:%M:%S',
                        time.localtime(time.time())), '服务端准备完毕，等待客户端连接')
    # 接收客户端的消息及客户端地址
    data, address = s.recvfrom(1024)
    print(time.strftime('%Y-%m-%d %H:%M:%S',
                        time.localtime(time.time())), '服务端收到来自客户端%s的消息：%s' % (address, data.decode('utf-8')))
    # 向客户端发送消息
    s.sendto('你好，我是服务端'.encode('utf-8'), address)
    s.close()
except Exception as e:
    print('创建UDP服务端失败', e)
