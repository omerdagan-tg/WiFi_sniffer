import os
import enum

class ProtocolFilteringOptions(enum.Enum):
    HTTP = "http"
    TCP = "TCP"
    UDP = "UDP"



class WifiMonitoringProgram:
    WifiAdapterName = 'wlan0'       #temporary adapter name

    global WifiAdapterName

    def __init__(self):
        pass        #init will read the ini file sent from the Host PC

    def startMonitoring(self, filterOption):
        os.system('airmon-ng check kill')  # killing processes that stop the airmon-ng from changing adapter to monitor mode
        os.system('airmon-ng start' + WifiAdapterName)  # changing the WiFi adapter to monitor mode
        os.system('tshark -i' + WifiAdapterName + '-w capture-output.pcap')  # saving the packets that the adapter sniffed
        os.system('tshark -2 -R  "-y ' + filterOption + '"  -r capture-output.pcap -T json >output.json')

    def stopMonitoring(self):
        os.system('airmon-ng stop' + WifiAdapterName)       #changing the WiFi adapter to stationary mode
        os.system('service network-manager start')      #restarting the processes that were killed when starting