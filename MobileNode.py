import socket
import sys
import time
import string
import utils

def server(port,homeAgentAddress, homeAgentPort,foreignAgent1Address,foreignAgent1Port,foreignAgent2Address, foreignAgent2Port):
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.settimeout(5)
    s.bind(("",port))
    sockName = s.getsockname()
    print sockName
    utils.sendData(homeAgentAddress,homeAgentPort,"2|"+foreignAgent1Address+"|"+str(foreignAgent1Port))
    nextSwitchTime = time.time()+5
    while True:
        
        data,address = s.recvfrom(1024)
        print "Sequence Number = %s Time = %s FA = %s Accepted" %(data,time.time(),address)
            
        if time.time() >= nextSwitchTime:
            foreignAgent1Address,foreignAgent2Address = foreignAgent2Address,foreignAgent1Address
            foreignAgent1Port,foreignAgent2Port = foreignAgent2Port,foreignAgent1Port
            utils.sendData(homeAgentAddress,homeAgentPort,"2|"+foreignAgent1Address+"|"+str(foreignAgent1Port))
            print "Registration sent.  Time = %s  New care-of address = %s/%d " %(time.time(),foreignAgent1Address,foreignAgent1Port)
            nextSwitchTime = time.time()+5
            
    s.close()  


server(int(sys.argv[1]),sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]),sys.argv[6], int(sys.argv[7]))


