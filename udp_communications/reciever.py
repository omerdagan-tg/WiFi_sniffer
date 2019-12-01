# ----- receiver.py -----

from socket import *
import sys
import select

host = "0.0.0.0"       # IP for all available network interfaces in current machine
port = 9999
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host, port))

addr = (host, port)
buf = 1024

name, addr = s.recvfrom(300)        # Gets name
name = name.strip()
name = name.decode()
name = name.replace("0", "").strip()
name = "new_" + name
print("Received File Name:", name)


size, addr = s.recvfrom(9)      # Gets size
size = size.strip()
size = int(size.decode())
print("Received File Size:", size)


f = open(name, 'wb')

cur_size = 0

try:
    while(cur_size < size):     # Write to a new file
        data, addr = s.recvfrom(buf)
        f.write(data)
        # s.settimeout(.2)
        cur_size = cur_size + len(data)


finally:
    f.close()
    s.close()
    print("File Downloaded")