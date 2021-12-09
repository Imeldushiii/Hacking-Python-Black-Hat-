import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))
host = f'Connection from: {socket.gethostname()}'
client.send(host.encode('ascii'))
def claim():
    while True:
        try:
            xd = f'Message: {input("Napisz cos: ")}'
            client.send(xd.encode('ascii'))
        except:
            client.close()
            break
claim()
