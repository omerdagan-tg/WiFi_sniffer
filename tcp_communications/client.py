import socket
import sys
import protocol

HOST_IP = "127.0.0.1"
PORT = 12345
BUFFER = 1024


def main():
    """implements the conversation with server"""
    # Open client socket, Transport layer: protocol TCP, Network layer: protocol IP
    client_socket = socket.socket()
    client_socket.connect((HOST_IP, PORT))
    try:
        while True:

            # Get request from keyboard
            client_request_str = input("Enter your command [Name]/.../[Exit]: ")
            if client_request_str:   # if client_request_str not empty string
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
