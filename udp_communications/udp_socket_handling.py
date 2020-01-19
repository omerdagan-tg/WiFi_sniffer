from socket import *
import sys
import select

# function get_input(), defined in sender.py, shouldn't be part of this class


class MySocket:
    def __init__(self, ip, port, buffer):
        self.addr = (ip, port)
        self.buffer = buffer

    # This function will be used by the udp client on the RPi

    def send(self, file_name, size):  # The name will be the date and time of the captured packets
        # we don't need address because we can store the file in a static place on the RPi

        s = socket(AF_INET, SOCK_DGRAM)

        file_name = file_name.zfill(300).encode()
        s.sendto(file_name, addr)           # Sends the file's name

        str_size = str(size).zfill(9).encode()
        s.sendto(str_size, addr)

        # note that getting the size and the name are defined in sender.py.
        # another class will handle getting this information.

        f = open(file_name, "rb")
        data = f.read(buf)
        while (data):
            if (s.sendto(data, addr)):
                print("sending...")
                data = f.read(buf)

        s.close()
        f.close()


    # This function will be used by the UDP server on the HPC
    def listen(self):





