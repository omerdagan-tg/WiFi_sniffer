import os

class Tshark:
    packetLocation = 'capture-output.pcap'
    def startMonitoring(self, WifiAdapterName):
        os.system('tshark -i' + WifiAdapterName + '-w' + self.packetLocation)  # saving the packets that the adapter sniffed


    def stopMonitoring(self):
        os.system('service network-manager start')  # restarting the processes that were killed when starting

    def getPacketLocation(self):
        return self.packetLocation
