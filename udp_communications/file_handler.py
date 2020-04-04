import os


class FileHandler:
    def __init__(self, name, data=None):
        self.data = data
        self.name = name

    def length(self):
        return os.stat(self.name).st_size

    def write(self):
        with open(self.name, 'wb') as f:  # needs to get a path from the user.
            for data in self.data:
                f.write(data)
        print("File Downloaded")

    def read(self, buffer):
        self.data = []
        with open(self.name, "rb") as f:
            cur_data = f.read(buffer)
            while cur_data:
                self.data.append(cur_data)
                print("reading")
                cur_data = f.read(buffer)
        return self.data






