import socket
import os
import tcp_communications.protocol as protocol

HOST_IP = "127.0.0.1"
PORT = 12345
BUFFER = 1024


def main():
    """implements the conversation with server"""
    # Open client socket, Transport layer: protocol TCP, Network layer: protocol IP
    client_socket = socket.socket()
    client_socket.connect((HOST_IP, PORT))
    ini_file_size = os.path.getsize("configuration.ini")
    try:
        while True:

            # Get request from keyboard
            client_request_str = input("Enter your command [Name]/.../[Exit]: ")
            if client_request_str:   # if client_request_str not empty string
                if client_request_str == 'configure':
                    client_socket.send("configure".encode())
                    client_socket.send(str(ini_file_size).encode())
                    with open('./configuration.ini', 'rb') as fs:
                        data = fs.read(1024)
                        while data:
                            client_socket.send(data)
                            data = fs.read(1024)
                # send request according to the protocol
                protocol.send_request(client_socket, client_request_str)
                # Get response from server
                response = protocol.get_response(client_socket)
                if response and response != "Bye!":
                    print("Server say:", response)
                else:
                    if not response:
                        print("Server crashes")
                    break
    finally:
        client_socket.close()

if __name__ == '__main__':
    main()
