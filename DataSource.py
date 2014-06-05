import socket
import sys
import time
import utils

def main(host,port):
    seqNumber = 1
    while True:
        utils.sendData(host,port,"1|"+ str(seqNumber))
        print "Sequence Number = %d Time = %s Dest = %s/%d" %(seqNumber, time.time(),socket.gethostbyname(host),port)
        time.sleep(1)
        seqNumber += 1
    
main(sys.argv[1],int(sys.argv[2])) 
#main("localhost",5000)


