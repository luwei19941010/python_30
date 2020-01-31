#-*-coding:utf-8-*-
# Author:Lu Wei

import os,hashlib,socket,struct

def MD5(s):
    secert='luwei'
    obj=hashlib.md5(secert.encode('utf-8'))
    obj.update(s)
    return  obj.hexdigest()

sk=socket.socket(type=socket.SOCK_STREAM)
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr=sk.accept()
random_num=os.urandom(32)
conn.send(random_num)

pack_size=conn.recv(4)
data_size=struct.unpack('i',pack_size)[0]
data=conn.recv(data_size).decode('utf-8')
md5_num=MD5(random_num)
if md5_num==data:
    print('ok')
