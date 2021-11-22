#Creator Szymon "Imeldushiii" Kubiak

import socket
import threading
from datetime import datetime
def results(ports, times):
    for i in ports:
        try:
            print(f'[+] Port: {i} Service: {socket.getservbyport(i)} ')
        except:
            print(f'[+] Port: {i}')
    print(f'Time : {times}')
def scan(i, final):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #Create TCP
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Manipulates socket options
    try:
        s.connect(("192.168.1.20", i))
        final.append(i)
    except:
        pass
def start_port():
    threads = []
    final = []
    t1 = datetime.now()
    for ints in range(10000):
        th = threading.Thread(target=scan, args=(ints, final))
        threads.append(th)
    for i in range(10000):   #do 10 000 times because limit of threads in 10 000!!
        threads[i].start()   #perform functions 10,000 times
    t2 = datetime.now()      #the time when the scan is over
    time_result = t2 - t1    #start time - actuall time
    results(final, time_result)    #start def results()
def main():                   #function that starts everything
   start_port()               #start function def start_port()
if __name__ == '__main__':    #to keep the script from executing by itself
    main()                    #start function def main()
