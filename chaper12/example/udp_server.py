# udp_server.py
#!/usr/bin/env python3
import socket
import os

# 使用UDP协议
s = socket.socket(type=socket.SOCK_DGRAM)
hostname = socket.gethostname()
# 绑定套接字地址
s.bind((hostname, 8888))
print('服务端已准备好')
try:
    while True:
        command = s.recv(1024).decode('utf-8')
        if command:
            print('服务端接收到命令：', command)
            if os.system(command).encode('utf-8') == 0:
                s.sendto('操作成功'.encode('utf-8'), (hostname, 8888))
            else:
                s.sendto('操作失败'.encode('utf-8'), (hostname, 8888))
        else:
            break
except Exception as e:
    print('创建UDP服务端失败', e)
finally:
    s.close()
