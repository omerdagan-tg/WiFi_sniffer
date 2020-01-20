class ini_protocol:
    start = 'START'
    end = 'END'
    protocols = 'PROTOCOLS'
    ip = 'IP'
    mac = 'MAC'

    def __init__(self, start, end, protocols, ip, mac):
        self.start = start
        self.end = end
        self.protocols = protocols
        self.ip = ip
        self.mac = mac