from socket import *
import json
from udp_communications.udp_data_utilization import *
import time


class UDPCommunication:

    BUFFER = 1024

    def __init__(self, ip, port, buffer=None):
        self.addr = (ip, port)
        self.buffer = buffer
        if buffer is None:
            self.buffer = UDPCommunication.BUFFER


    # This function will be used by the udp client on the RPi

    def send(self, file_name):  # The name will be the date and time of the captured packets
        # we don't need address because we can store the file in a static place on the RPi

        data_handler = DataUtilization(file_name)

        s = socket(AF_INET, SOCK_DGRAM)
        data = data_handler.send_data(self.buffer)
        while(data):
            s.sendto(data, self.addr)
            print("sending")
            data = data_handler.send_data(self.buffer)

        s.close()

    # This function will be used by the UDP server on the HPC
    def listen(self):
        handle_data = DataUtilization().get_data
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(self.addr)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        while True:
            data, addr = s.recvfrom(self.buffer)
            if data.strip() == b'bye':   # signal to close the server socket
                break
            handle_data(data)
        s.close()

    #sends a file every number of seconds (provided by arguments)
    def send_with_timer(self, file_name, sec):
        while True:
            time.sleep(sec)
            self.send(file_name)
            os.remove(file_name)