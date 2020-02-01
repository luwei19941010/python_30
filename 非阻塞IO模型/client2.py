#-*-coding:utf-8-*-
# Author:Lu Wei
import socket
import time
sk=socket.socket(type=socket.SOCK_STREAM)

sk.connect(('127.0.0.1',9000))
while True:
    time.sleep(1)
    sk.send('clent22'.encode('utf-8'))
    a=print(sk.recv(1024).decode('utf-8'))