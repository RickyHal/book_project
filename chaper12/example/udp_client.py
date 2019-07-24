# upfile_client.py
#!/usr/bin/env python3
import socket

s = socket.socket(type=socket.SOCK_DGRAM)
hostname = socket.gethostname()
command = input('请输入命令：')
try:
    while command:
        s.sendto(command.encode('utf-8'), (hostname, 8888))
        print(s.recv(1024).decode('utf-8'))
        command = input('请输入命令：')
except Exception as e:
    print('创建UDP客户端失败', e)
finally:
    s.close()
