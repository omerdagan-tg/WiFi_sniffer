import os


list = ["tcp", "udp", "arp"]


def get_configurations():     # configurations from the user
    pass


def update_ini(list):   # the list is a list of configurations, in the future we'll have more lists.
    f = open(r"..\tcp_communications\client\configuration.ini", "w")    # path to ini file
    f.write("START\n")
    f.write("PROTOCOL\n")
    for i in list:      # write the protocols to sniff
        f.write(i + "\n")

    f.write("END")      # end of ini file
    f.close()


update_ini(list)



