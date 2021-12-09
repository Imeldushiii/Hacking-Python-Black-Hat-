import socket
import threading
host = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
def ill(client):
    while True:
        msg = client.recv(2048).decode('ascii')
        print(msg)
while True:
    client, address = server.accept()
    print(f'Connection from: {address}')
    ill(client)

