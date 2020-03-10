from socket import *
import json


class DataUtilization:

    def __init__(self):
        self.name = None
        self.size = -1
        self.current_size = 0
        self.data = []
        self.isData = False

    def init(self):     # will be used to initialize after use
        self.cur_size = 0
        self.name = None
        self.size = -1
        self.current_size = 0
        self.data = []
        self.isData = False

    def save_file(self):
        with open(self.name, 'wb') as f:  # needs to get a path from the user.
            for data in self.data:
                f.write(data)
        print("File Downloaded")
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
