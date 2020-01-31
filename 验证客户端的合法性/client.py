#-*-coding:utf-8-*-
# Author:Lu Wei

import os,hashlib,socket,struct

def MD5(s):
    secert='luwei'
    obj=hashlib.md5(secert.encode('utf-8'))
    obj.update(s)
    return  obj.hexdigest()

sk=socket.socket(type=socket.SOCK_STREAM)
sk.connect(('127.0.0.1',9000))

random_num=sk.recv(32)
data=MD5(random_num)

size=struct.pack('i',len(data))
sk.send(size)
sk.send(data.encode('utf-8'))
