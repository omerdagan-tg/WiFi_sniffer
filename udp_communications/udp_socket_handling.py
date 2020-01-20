from socket import *
import sys
import select

# function get_input(), defined in sender.py, shouldn't be part of this class


# def check_for_signal():  # Gets a signal to close the server
#   pass

# Not sure who is supposed to handle this function

class MySocket:
    NAME_ZFILL = 300
    LENGTH_ZFILL = 9
    def __init__(self, ip, port, buffer):
        self.addr = (ip, port)
        self.buffer = buffer

    # This function will be used by the udp client on the RPi

    def send(self, file_name, size):  # The name will be the date and time of the captured packets
        # we don't need address because we can store the file in a static place on the RPi

        s = socket(AF_INET, SOCK_DGRAM)

        file_name = file_name.zfill(MySocket.NAME_ZFILL).encode()
        s.sendto(file_name, self.addr)           # Sends the file's name

        str_size = str(size).zfill(MySocket.LENGTH_ZFILL).encode()
        s.sendto(str_size, self.addr)

        # note that getting the size and the name are defined in sender.py.
        # another class will handle getting this information.

        f = open(file_name, "rb")
        data = f.read(self.buffer)
        while (data):
            if (s.sendto(data, self.addr)):
                print("sending...")
                data = f.read(self.buffer)

        s.close()
        f.close()


    # This function will be used by the UDP server on the HPC
    def listen(self):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(self.addr)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        while (not signal):     # again, not sure who should handle this
            name, addr = s.recvfrom(MySocket.NAME_ZFILL)  # Gets name
            name = name.strip()
            name = name.decode()
            name = name.replace("0", "").strip()
            name = "new_" + name
            print("Received File Name:", name)

            size, addr = s.recvfrom(MySocket.LENGTH_ZFILL)  # Gets size
            size = size.strip()
            size = int(size.decode())
            print("Received File Size:", size)

            f = open(name, 'wb')

            cur_size = 0

            try:
                while (cur_size < size):  # Write to a new file
                    data, addr = s.recvfrom(self.buffer)
                    f.write(data)
                    # s.settimeout(.2)
                    cur_size = cur_size + len(data)
            finally:
                f.close()
                print("File Downloaded")
            signal = check_for_signal()  # Will be developed later on

        s.close()











