try:
    import socket
except:
    print("[-] Nie zainstalowano biblioteki Python ")
f = open("index.html", "r")
tekst = f.read()
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('192.168.1.20', 80)) #twoje IP
mySocket.listen(5)
while True:
    (recvSocket, address) = mySocket.accept()
    print(f'[+] Połączenie od: {recvSocket.recv(1024)}')
    recvSocket.send(bytes(tekst.encode()))
    recvSocket.close()