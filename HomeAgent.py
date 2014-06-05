import socket
import sys
import time
import string
import utils

def server(port):
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("",port))
    sockName = s.getsockname()
    print sockName
    foreignAgentAddress = None
    foreignAgentPort = None
    while True:
        data,address = s.recvfrom(1024)
        dataArray = string.split(data,"|")
        if dataArray[0] == "1":
            if foreignAgentAddress is None:
                print "Foreign Agent Address is unknown"
            else:
                utils.sendData(foreignAgentAddress,foreignAgentPort,dataArray[1])                   
                print "Sequence Number = %s Time = %s Forwarded to %s/%d " %(dataArray[1], time.time(),foreignAgentAddress,foreignAgentPort)
        elif dataArray[0] =="2":
            foreignAgentAddress = dataArray[1]
            foreignAgentPort = int(dataArray[2])
            print " Registration packet received.  Time =%s  Changing care-of address to %s/%d" %(time.time(),foreignAgentAddress,foreignAgentPort) 
        else:
            print dataArray
    s.close()  


server(int(sys.argv[1]))


