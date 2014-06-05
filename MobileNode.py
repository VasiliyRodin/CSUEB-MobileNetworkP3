import socket
import sys
import time
import string
import utils

def server(port,homeAgentAddress, homeAgentPort,foreignAgent1Address,foreignAgent1Port,foreignAgent1BindPort,foreignAgent2Address, foreignAgent2Port,foreignAgent2BindPort):
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.settimeout(5)
    s.bind(("",port))
    sockName = s.getsockname()
    print sockName
    utils.sendData(homeAgentAddress,homeAgentPort,"2|"+foreignAgent1Address+"|"+str(foreignAgent1Port))
    nextSwitchTime = time.time()+5
    while True:
        
        data,addressPair = s.recvfrom(1024)
        address,port = addressPair
        if address == socket.gethostbyname(foreignAgent1Address):
            status = "Accepted"
        else:
            status = "Rejected"
        print "Sequence Number = %s Time = %s FA = %s/%d %s" %(data,time.time(),address,port, status)
            
        if time.time() >= nextSwitchTime:
            foreignAgent1Address,foreignAgent2Address = foreignAgent2Address,foreignAgent1Address
            foreignAgent1Port,foreignAgent2Port = foreignAgent2Port,foreignAgent1Port
            foreignAgent1BindPort,foreignAgent2BindPort=foreignAgent2BindPort,foreignAgent1BindPort
            utils.sendData(homeAgentAddress,homeAgentPort,"2|"+foreignAgent1Address+"|"+str(foreignAgent1Port))
            print "Registration sent.  Time = %s  New care-of address = %s/%d " %(time.time(),foreignAgent1Address,foreignAgent1Port)
            nextSwitchTime = time.time()+5
            
    s.close()  


server(int(sys.argv[1]),sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), int(sys.argv[6]),sys.argv[7], int(sys.argv[8]),int(sys.argv[9]))


