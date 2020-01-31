### day30

### 今日内容

#### 1.socket的非阻塞io模型

​		通过socket的非阻塞io模型+io多路复用实现。，虽然非阻塞，提高了cpu利用率，但是消耗cpu做了很多无用功

```
#server
```



```
#client
```



#### 2.验证客户的合法性

```
#server

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
```

```
#client
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
```

#### 3.HMAC

```
import hmac
k1=b'asd'
v2=b'sad'
h=hmac.new(k1,v2)
print(h.digest())
#b'(\x0c\xe2H\xe8H\xbc\xd4\xe5\xa3\x1a\x03h)\xd1\x85' 长度16
```

#### 4.socket-server

```
import socketserver

class MYSERVER(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            msg=self.request.recv(1024).decode('utf-8')
            self.request.send(msg.upper().encode('utf-8'))

server=socketserver.ThreadingTCPServer(('127.0.0.1',9000),MYSERVER)
server.serve_forever()
```

