import socket
import sys
import time
import string

def server(port):
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("",port))
    sockName = s.getsockname()
    print sockName
    while True:
        data,address = s.recvfrom(1024)
        dataArray = string.split(data,"|")
        if dataArray[0] == "1":
            print "Sequence Number = %s Time = %s Forwarded to " %(dataArray[1], time.time())    
        elif dataArray[0] =="2":
            print " Registration packet received.  Time =  Changing care-of address to  "
        else:
            print dataArray
    s.close()  


server(int(sys.argv[1]))


