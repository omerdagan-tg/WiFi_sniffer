# ----- receiver.py -----

from socket import *
import sys
import select


def check_for_signal():  # Gets a signal to close the server
    pass

# Erez: Please refer to my notes in "sender.py"

host = "0.0.0.0"       # IP for all available network interfaces in current machine
port = 9999
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host, port))

buf = 1024

# When you create a socket, you don't really own it. The OS (TCP stack) creates it for you and gives you
#  a handle (file descriptor) to access it. When your socket is closed, it take time for the OS to "fully close it"
# socket.SO_REUSEADDR, causes the port to be released immediately after the socket is closed.
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

signal = False  # Needs to get a signal to close the server

while (not signal):
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
        print("File Downloaded")
    signal = check_for_signal()  # Will be developed later on


s.close()
