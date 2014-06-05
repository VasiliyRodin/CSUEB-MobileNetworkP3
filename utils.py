import socket

def sendData(address,port,data,bindPort=0):
    destSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    destSocket.bind(("",bindPort))
    hp = socket.gethostbyname(address)
    destSocket.sendto(data,(hp,port))
    destSocket.close() 
