import socket
import sys
import time

def server(port):
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("",port))
    sockName = s.getsockname()
    print sockName
    while True:
        data,address = s.recvfrom(1024)
        print "Sequence Number = %s Time = %s Forwarded to " %(data, time.time())
    s.close()  


server(int(sys.argv[1]))

#main("localhost",5000)
