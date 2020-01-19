from socket import *
import sys
import select

# function get_input(), defined in sender.py shouldn't be part of this class


class MySocket:
    def __init__(self, ip, port, buffer):
        self.addr = (ip, port)
        self.buffer = buffer



