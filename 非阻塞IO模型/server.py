#-*-coding:utf-8-*-
# Author:Lu Wei

import socket

sk=socket.socket(type=socket.SOCK_STREAM)
sk.bind(('127.0.0.1',9000))
sk.setblocking(False)
sk.listen()

l=[]
d_l=[]
while True:
    try:
        conn,addr=sk.accept()
        print(conn)
        l.append(conn)
    except BlockingIOError:
        for c in l:
            try:
                a=c.recv(1024).decode('utf-8')
                if not a:
                    d_l.append(c)
                    continue
                c.send(a.upper().encode('utf-8'))
            except BlockingIOError:pass
        for i in d_l:
            l.remove(i)
        d_l.clear()
