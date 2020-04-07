import os
import pyshark
import WMP.ini_protocol as ini_protocol



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
        for filename in os.listdir(self.packet_location):
            for ip_filter in self.IP:
                filtered_cap = pyshark.FileCapture(self.packet_location + filename, display_filter=ip_filter)
                if not filtered_cap:

                    os.remove(self.packet_location + filename)
                    
            for protocol_filter in self.protocols:
               filtered_cap = pyshark.FileCapture(self.packet_location + filename, display_filter=protocol_filter)
               if not filtered_cap:
                    os.remove(self.packet_location + filename)
                    os.remove(self.packet_location + filename)

            for protocol_filter in self.protocols:
                filtered_cap = pyshark.FileCapture(self.packet_location + filename, display_filter=protocol_filter)
                if not filtered_cap:
                    os.remove(self.packet_location + filename)
             
            for MAC_filter in self.MAC:
                filtered_cap = pyshark.FileCapture(self.packet_location + filename, display_filter=MAC_filter)
                if not filtered_cap:
                    os.remove(self.packet_location + filename)



    def configure_filter(self):
        current_filter = ''

        # Erez: You should noy parse ini files as text. Ini has standard rules and can be parsed using "configparser" library of Python.
        # Using libraries is the best way to avoid mistakes and Python is full with it so always keep it in mind.
        file = open(self.ini_location + '\configure.ini', 'r')
        file_txt = file.readlines()
        for line in file_txt:
            if line == ini_protocol.start:
                current_filter = ini_protocol.start
                self.isStarted = True
            elif line == ini_protocol.end:
                self.current_filter = ini_protocol.end
                self.isEnded = True
                break
            elif line == ini_protocol.protocols or current_filter == ini_protocol.protocol:
                current_filter = ini_protocol.protocol
                if line != ini_protocol.protocol:
                    self.protocols.append(line)
            elif line == ini_protocol.ip:
                current_filter = ini_protocol.ip
                if line != ini_protocol.ip:
                    self.IP.append(line)
            elif line == ini_protocol.mac or current_filter == ini_protocol.mac:
                current_filter = ini_protocol.mac
                if line != ini_protocol.mac:
                    self.MAC.append(line)


    def getMacs(self):
        return self.MAC

    def getProtocols(self):
        return self.protocols

    def getIP(self):
        return self.IP

    def getIniLocation(self):
        return self.ini_location

    def getPacketLocation(self):
        return self.packet_location

    def setIniLocation(self, ini_location):
        self.ini_location = ini_location

    def setPacketLocation(self, packet_location):
        self.packet_location = packet_location

