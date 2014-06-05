import socket
import sys
import time
import string
import utils

def server(foreignAgentPort, mobileNodeAddress, mobileNodePort):
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("",foreignAgentPort))
    sockName = s.getsockname()
    print sockName
    while True:
        data,address = s.recvfrom(1024)
        utils.sendData(mobileNodeAddress,mobileNodePort,data)
        print "Sequence Number = %s Time = %s Forwarded to %s/%d" %(data, time.time(),socket.gethostbyname(mobileNodeAddress),mobileNodePort)
    s.close()  


server(int(sys.argv[1]),sys.argv[2],int(sys.argv[3]))


