# ----- receiver.py -----

from socket import *
import sys
import select

host="0.0.0.0"
port = 9999
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf=1024

data,addr = s.recvfrom(300)
data = data.strip()
name = data.decode()
name = name.replace("0"," ").strip()
name = "new" + name
print ("Received File Name:",name)


data,addr = s.recvfrom(9)
data = data.strip()
size = int(data.decode())
print ("Received File Size:",size)


f = open(name,'wb')

cur_size = 0

try:
    while(cur_size < size):
        data, addr = s.recvfrom(buf)
        f.write(data)
        # s.settimeout(.2)
        cur_size = cur_size + len(data)


finally:
    f.close()
    s.close()
    print("File Downloaded")