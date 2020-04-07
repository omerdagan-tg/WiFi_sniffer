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
        packetLocation = Tshark.getPacketLocation()
        rpiConfigurationParser = RPiConfigParser(packet_location=packetLocation, ini_location= 'settings.ini')
        monitor = WifiMonitoringProgram()
        TCPserver = threading.Thread(target=tcpServer.startCommu, args=())
        UDPclient = udpClient("192.168.1.1", 12000)
        UDPclientThread = threading.Thread(target=UDPclient.send_with_timer, args=(packetLocation, 5))

        try:
            TCPserver.start()

        except:
            print ("Error: unable to start tcp server thread")



    def start(self):

        try:
            self.monitor.startMonitorMode()
        except:
            print("Error: unable to start monitor mode")

        try:
            self.UDPclientThread.start()

        except:
            print("Error: unable to start udp client thread")


