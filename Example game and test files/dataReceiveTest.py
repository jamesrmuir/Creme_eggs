#Receive data test
#Imports modules===============================================================#
import socket

#Variables=====================================================================#
targetIP = "127.0.0.1"
targetPort = 5005

#Sets up the socket
sock = socket.socket(socket.AF_INET, #Internet
                     socket.SOCK_DGRAM) #UDP
#Binds socket
sock.bind((targetIP, targetPort))

#While loop
while True:
    data, addr = sock.recvfrom(1024) # Buffer size is 1024
    print ("received message:", data)
