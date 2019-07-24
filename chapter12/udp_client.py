# udp_client.py
#!/usr/bin/env python3
import socket
import time

try:
    s = socket.socket(type=socket.SOCK_DGRAM)
    hostname = socket.gethostname()
    data = '你好，我是客户端'.encode('utf-8')
    # 向服务端发送消息
    s.sendto(data, (hostname, 8888))
    # 接收服务端的消息
    response, address = s.recvfrom(1024)
    print(time.strftime('%Y-%m-%d %H:%M:%S',
                        time.localtime(time.time())), '收到服务端%s的消息：%s' % (address, response.decode('utf-8')))
    s.close()
except Exception as e:
    print('创建UDP客户端失败', e)
