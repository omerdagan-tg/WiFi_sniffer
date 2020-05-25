from socket import *
import json
import udp_communications.file_handler as FileHandler


class DataUtilization:

    def __init__(self, name=None):
        self.name = name
        self.size = -1
        self.current_size = 0
        self.data = []
        self.isData = False

    def init(self):     # will be used to initialize after get_data() use
        self.cur_size = 0
        self.name = None
        self.size = -1
        self.current_size = 0
        self.data = []
        self.isData = False

    def save_file(self):
        file_handler = FileHandler(self.name, self.data)
        file_handler.write()
        self.init()

    def get_data(self, data):
        if not self.isData:  # The first thing that will be sent is the name and size
            data = data.strip()
            try:
                data_str = data.decode()
                try:
                    json_object = json.loads(data_str)
                    # we got file name and size
                    self.name = json_object["name"]
                    print("Received File Name:", self.name)
                    self.size = int(json_object["size"])
                    print("Received File Size:", self.size)
                    self.current_size = 0
                    self.isData = True

                except ValueError as e:
                    print("need your check")

            except UnicodeDecodeError as er:
                print("something went wrong")
        else:
            try:
                # we got file data
                self.data.append(data)
                self.current_size = self.current_size + len(data)

                if self.current_size >= self.size:
                    # save to file
                    self.save_file()

            except ValueError as e:
                print("need your check")

    def send_data(self, buffer):

        file_handler = FileHandler(self.name)

        if self.size == -1:
            self.size = file_handler.length()
            print(self.size)
            message = {"name": "new_"+self.name, "size": self.size}
            message = json.dumps(message).rjust(buffer)
            message = message.encode()
            self.data = file_handler.read(buffer)
            self.isData = True
            return message

        elif self.isData is True:
            if self.data:
                message = self.data.pop(0)
                return message
            else:
                self.init()
                return None

