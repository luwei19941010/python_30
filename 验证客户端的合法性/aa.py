#-*-coding:utf-8-*-
# Author:Lu Wei
import os,hashlib,hmac
# a=os.urandom(32)
#
# print(a)

# a=b'\x047Km}\x01f\x16\x85\x08\x05c\xd2\xfer\x06\xfd_\x9dW4c\tM?\xbe|q<\x88\xe5\xcb'
# print(str(a))
# def MD5(s):
#     secert='luwei'
#     obj=hashlib.md5(secert.encode('utf-8'))
#     obj.update(s)
#     return  obj.hexdigest()
# print(MD5(a))

#2d84381689746a2cacc25ca778f316b0
k1=b'asd'
v2=b'sad'
h=hmac.new(k1,v2)
print(h.digest())
