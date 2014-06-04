import socket
import sys
import time

def main(host,port):
    seqNumber = 1
    while True:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("",0))
        hp = socket.gethostbyname(host)
        s.sendto("1|"+ str(seqNumber),(hp,port))
        s.close()
        print "Sequence Number = %d Time = %s Dest = %s/%d" %(seqNumber, time.time(),hp,port)
        time.sleep(1)
        seqNumber += 1
    
main(sys.argv[1],int(sys.argv[2]))
#main("localhost",5000)


