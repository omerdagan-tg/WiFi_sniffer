import os
import pyshark

class RpiConfigurationParser:
    isStarted = False
    isEnded = False
    ini_location = ''
    packet_location = ''
    IP = []
    protocols = []
    MAC = []

    def __init__(self, ini_location, packet_location):
        self.ini_location = ini_location
        self.packet_location = packet_location

    def filter(self):
        global packet_location
        global IP
        global protocols
        global MAC
        for filename in os.listdir(packet_location):
            for ip_filter in IP:
                filtered_cap = pyshark.FileCapture(packet_location + filename, display_filter=ip_filter)
                if not filtered_cap:
                    os.remove(packet_location + filename)
                    
             for protocol_filter in protocols:
                filtered_cap = pyshark.FileCapture(packet_location + filename, display_filter=protocol_filter)
                if not filtered_cap:
                    os.remove(packet_location + filename)
             
            for MAC_filter in MAC:
                filtered_cap = pyshark.FileCapture(packet_location + filename, display_filter=MAC_filter)
                if not filtered_cap:
                    os.remove(packet_location + filename)



    def configure_filter(self):
        global ini_location
        global isStarted
        global isEnded
        global protocols
        global IP
        global MAC
        current_filter = ''

        file = open(ini_location + '\configure.ini', 'r')
        file_txt = file.readlines()
        for line in file_txt:
            if line == 'START':
                current_filter = 'START'
                isStarted = True
            elif line == 'END':
                current_filter = 'END'
                isEnded = True
                break
            elif line == 'PROTOCOLS' or current_filter == 'PROTOCOLS':
                current_filter = 'PROTOCOLS'
                if line != 'PROTOCOLS':
                    protocols.append(line)
            elif line == 'IP':
                current_filter = 'IP'
                if line != 'IP':
                    IP.append(line)
            elif line == 'MAC' or current_filter == 'MAC':
                current_filter = 'MAC'
                if line != 'MAC':
                    MAC.append(line)





