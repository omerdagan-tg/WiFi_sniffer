
import socket               # Import socket module

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip = "0.0.0.0" # Get local machine name
port = 12345                 # Reserve a port for your service.
server_socket.bind((ip, port))        # Bind to the port
server_socket.listen(1)                 # Now wait for client connection.
print("server online")
while True:

    client_socket, addr = server_socket.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    msg_size = client_socket.recv(1024).decode()
    print("size of file=",msg_size)
    file_size = int(msg_size)
    current_size = 0

    with open("masknew.gif", 'wb') as fw:

        while True:
            data = client_socket.recv(1024)
            current_size = current_size + len(data)
            fw.write(data)
            if current_size >= file_size:
                print('end writing')
                break
    client_socket.send("end recv".encode())
client_socket.close()