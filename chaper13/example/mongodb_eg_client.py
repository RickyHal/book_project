# mongodb_eg_client.py
#!/usr/bin/env python3
import socket


if __name__ == "__main__":
    message = input('您：')
    client = socket.socket()
    client.connect((socket.gethostname(), 8888))
    while message != 'bye':
        client.send(message.encode('utf-8'))
        print('机器人:', client.recv(1024).decode('utf-8'))
        message = input('您：')
    client.close()
