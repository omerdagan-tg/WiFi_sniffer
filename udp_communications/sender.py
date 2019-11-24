# ----- sender.py ------


from socket import *
import sys

def get_input():  # Gets the json file through pipe
    pass


s = socket(AF_INET, SOCK_DGRAM)
host = "127.0.0.1"
port = 9999
buf =1024
addr = (host,port)

file_name = "mask.gif"


f=open(file_name,"rb")

file_name = "mask.gif".zfill(300).encode()
s.sendto(file_name,addr)

all_data = data = f.read(buf)
while (data):
    data = f.read(buf)
    all_data += data
size = len(all_data)
str_size = str(size).zfill(9).encode()
s.sendto(str_size,addr)

f.seek(0)
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print("sending...")
        data = f.read(buf)

s.close()
f.close()