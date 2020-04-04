import os

class Tshark:
    def startMonitoring(self, WifiAdapterName):
        os.system('tshark -i' + WifiAdapterName + '-w capture-output.pcap')  # saving the packets that the adapter sniffed


    def stopMonitoring(self):
        os.system('service network-manager start')  # restarting the processes that were killed when starting