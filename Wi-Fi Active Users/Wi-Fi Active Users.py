#Creator Szymon "Imeldushiii" Kubiak
import socket
import threading
import subprocess as p
import re
def results(all):
    for x in all:
        ip = x[0]
        command = p.run(['ping', ip, '-n','1'],capture_output=True).stdout.decode()
        search = re.search("TTL=(.*)\r", command)
        if search == None:
            print(f'[+] Device: {x[0]} IP: {x[2]} Status: Down')
        else:
            print(f'[+] Device: {x[0]} IP: {x[2]} Status: UP')
def scanuj(ints, tablica):
    try:
        ip = socket.gethostbyaddr("192.168.1." + str(ints))
        tablica.append(ip)
    except:
        pass
def odpalaj():
    threads = []
    final = []
    for i in range(255):
        th = threading.Thread(target=scanuj, args=(i, final))
        threads.append(th)
    for i in range(255):
        threads[i].start()
    results(final)
def main():
    odpalaj()
if __name__ == '__main__':
    main()
