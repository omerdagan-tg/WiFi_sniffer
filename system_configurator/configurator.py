import os


list = ["tcp", "udp", "arp"]


def get_configurations():     # configurations from the user
    pass


def update_ini(list):   # the list is a list of configurations
    f = open(r"..\tcp_communications\client\configuration.ini", "w")    # path to ini file
    f.write("start\n")
    for i in list:
        f.write(i + "\n")
    f.write("end")
    f.close()


update_ini(list)



