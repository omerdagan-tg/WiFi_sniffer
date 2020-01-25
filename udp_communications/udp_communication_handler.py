from socket import *
import json


class UDPCommunicationHandler:

    BUFFER = 1024

    def __init__(self, ip, port, buffer=None):
        self.addr = (ip, port)
        self.buffer = buffer
        if buffer is None:
            self.buffer = UDPCommunicationHandler.BUFFER


    # This function will be used by the udp client on the RPi - NOT FIXED

    def send(self, file_name, size):  # The name will be the date and time of the captured packets
        # we don't need address because we can store the file in a static place on the RPi

        s = socket(AF_INET, SOCK_DGRAM)

        json_object = {"name": file_name, "size": str(size)}
        json_str = json.dumps(json_object)
        str_to_send = json_str.rjust(self.bufffer)
        s.sendto(str_to_send.encode(), self.addr)

        # note that getting the size and the name are defined in sender.py.
        # another class will handle getting this information.

        with open(file_name, "rb") as f:
            data = f.read(self.buffer)
            while (data):
                if (s.sendto(data, self.addr)):
                    print("sending...")
                    data = f.read(self.buffer)

        s.close()

    # This function will be used by the UDP server on the HPC
    def listen(self, handle_data):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(self.addr)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        while True:
            data, addr = s.recvfrom(self.buffer)
            if data.strip() == b'bye':
                break
            handle_data(data)
        s.close()