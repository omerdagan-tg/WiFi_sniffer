import WMP.RPi_configuration_parser as RPiConfigParser
import WMP.Tshark as Tshark
from WMP.WifiMonitoringProgram import WifiMonitoringProgram
import tcp_communications.server.server as tcpServer
from udp_communications.udp_communication_handler import UDPCommunication as udpClient
from WMP.RPi_configuration_parser import RpiConfigurationParser as RPiConfigParser
from WMP.Tshark import Tshark
import threading

class ControlApp:
    def __init__(self):
        self.packetLocation = Tshark.getPacketLocation()
        self.rpiConfigurationParser = RPiConfigParser(packet_location=self.packetLocation, ini_location= 'settings.ini')
        self.monitor = WifiMonitoringProgram()
        self.TCPserver = threading.Thread(target=tcpServer.startCommu, args=())
        self.UDPclient = udpClient("192.168.1.1", 12000)
        self.UDPclientThread = threading.Thread(target=self.UDPclient.send_with_timer, args=(self.packetLocation, 5))

        try:
            self.TCPserver.start()

        except:
            print ("Error: unable to start tcp server thread")



    def start(self):

        try:
            self.monitor.startMonitorMode()
        except:
            print("Error: unable to start monitor mode")

        try:
            Tshark.startMonitoring()

        except:
            print("Error: unable to start monitoring")

        try:
            self.UDPclientThread.start()

        except:
            print("Error: unable to start udp client thread")



    def pause(self):
        try:
            Tshark.stopMonitorMode()
        except:
            print("Error: unable to stop monitor mode")


    def stop(self):
        try:
            self.monitor.stopMonitorMode()
        except:
            print("Error: unable to stop monitor mode")

        try:
            Tshark.stopMonitoring()

        except:
            print("Error: unable to stop monitoring")

        try:
            self.UDPclientThread._stop()

        except:
            print("Error: unable to stop udp client thread")
