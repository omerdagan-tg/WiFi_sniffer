import os

class WifiMonitoringProgram:
    WifiAdapterName = 'wlan0'       #default adapter name

    def __init__(self):
        pass        #init will read the ini file sent from the Host PC

    def startMonitorMode(self, WifiAdapterName):
        self.WifiAdapterName = WifiAdapterName
        os.system('airmon-ng check kill')  # killing processes that stop the airmon-ng from changing adapter to monitor mode
        os.system('airmon-ng start' + self.WifiAdapterName)  # changing the WiFi adapter to monitor mode


    def startMonitorMode(self):
        os.system('airmon-ng check kill')  # killing processes that stop the airmon-ng from changing adapter to monitor mode
        os.system('airmon-ng start' + self.WifiAdapterName)  # changing the WiFi adapter to monitor mode

    def stopMonitorMode(self, WifiAdapterName):
        self.WifiAdapterName = WifiAdapterName
        os.system('airmon-ng stop' + self.WifiAdapterName)  # changing the WiFi adapter to stationary mode

    def stopMonitorMode(self):
        os.system('airmon-ng stop' + self.WifiAdapterName)  # changing the WiFi adapter to stationary mode