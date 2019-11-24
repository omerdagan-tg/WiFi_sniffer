import os, socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
ip = "localhost" # Get local machine name
port = 12345                 # Reserve a port for your service.

client_socket.connect((ip, port))

print ('Sending...')

file_size = os.path.getsize("mask.gif")
print(file_size)
client_socket.send(str(file_size).encode())

with open('./mask.gif', 'rb') as fs:
    data = fs.read(1024)
    while data:
        client_socket.send(data)
        data = fs.read(1024)
mes = client_socket.recv(1024)
print(mes.decode())
client_socket.close()