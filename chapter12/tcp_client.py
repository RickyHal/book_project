# tcp_client.py
#!/usr/bin/env python3
import socket
import time

try:
    s = socket.socket()
    hostname = socket.gethostname()
    s.connect((hostname, 8888))
    # 接收服务端消息并解码
    response = s.recv(1024).decode('utf-8')
    print(time.strftime('%Y-%m-%d %H:%M:%S',
                        time.localtime(time.time())), '收到服务端消息：', response)
    # 关闭套接字
    s.close()
except Exception as e:
    print('建立TCP客户端失败', e)
