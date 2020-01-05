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
        # Erez:  Regarding globals in programming - Don't ever use them. (Unless in very very very few cases)
        # Why? the function should not be aware from the outside world because than if changes occur outside of this functions it would break.
        # Globals is super dangerous from many reasons so if only this function is using these variables so receive them as argument
        # if the entire class is using them, then receive them in the class constructor
        # If you want other modules to access them, you should add a function for example "getMacs" that returns a copy of all the MAC addresses you got.
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
        # See my comment regarding globals aboce
        global ini_location
        global isStarted
        global isEnded
        global protocols
        global IP
        global MAC
        current_filter = ''

        # Erez: You should noy parse ini files as text. Ini has standard rules and can be parsed using "configparser" library of Python.
        # Using libraries is the best way to avoid mistakes and Python is full with it so always keep it in mind.
        file = open(ini_location + '\configure.ini', 'r')
        file_txt = file.readlines()
        for line in file_txt:
            # Erez: All the keywords such as START, END, IP, MAC are a part of your protocol, and should be defined in a seperate file and pulled from there instead of written hard coded.
            # for example instead of line == 'STRAT' I would like to see line == clientProtocol.start. This way you will be on the safe side that you spelled it right, and you'll be safe from changes.
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





