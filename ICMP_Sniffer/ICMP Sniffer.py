#CREATOR SZYMON 'IMELDUSHII' KUBIAK
import socket
import os
import threading
HOST = '192.168.1.20' #HOST
def icmp():
    if os.name == 'nt':
      socket_protocol = socket.IPPROTO_IP
    else:
      socket_protocol = socket.IPPROTO_ICMP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW,socket_protocol)
    sniffer.bind((HOST, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    if os.name == 'nt':
     sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    output = sniffer.recvfrom(65565)
    try:
        print(f'[+] -> {output[1][0]}')
    except:
        print(f'[-] -> {output[1][0]}')
    if os.name == 'nt':
     sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
while True:
     icmp()
