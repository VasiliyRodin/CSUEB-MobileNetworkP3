import socket

def sendData(address,port,data):
    destSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    destSocket.bind(("",0))
    hp = socket.gethostbyname(address)
    destSocket.sendto(data,(hp,port))
    destSocket.close() 
