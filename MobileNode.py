import socket
import sys
import time
import string
import utils

def server(port,homeAgentAddress, homeAgentPort,foreignAgent1Address,foreignAgent1Port,foreignAgent2Address, foreignAgent2Port):
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(5)
    s.bind(("",port))
    sockName = s.getsockname()
    print sockName
    utils.sendData(homeAgentAddress,homeAgentPort,"2|"+foreignAgent1Address+"|"+foreignAgent1Port)
    while True:
        try:
            data,address = s.recvfrom(1024)
            print "Sequence Number = %s Time = %s FA = %s Accepted" %(data,time.time(),address)
            
        except socket.timeout:
            foreignAgent1Address,foreignAgent2Address = foreignAgent2Address,foreignAgent1Address
            foreignAgent1Port,foreignAgent2Port = foreignAgent2Port,foreignAgent1Port
            utils.sendData(homeAgentAddress,homeAgentPort,"2|"+foreignAgent1Address+"|"+foreignAgent1Port)
            print "Registration sent.  Time = %s  New care-of address = %s/%d " %(time.time(),foreignAgent1Address,foreignAgent1Port)
            
            
  s.close()  


server(int(sys.argv[1]),sys.argv[2], int(sys.argv[4]), sys.argv[3], int(sys.argv[5]),sys.argv[6], int(sys.argv[7]))


