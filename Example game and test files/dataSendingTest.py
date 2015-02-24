#Send file test
#Imports modules===============================================================#
import socket

#Variables=====================================================================#
#Defines target ip and ports
targetIP = "127.0.0.1"
targetPort = 5005

#Defines data to send
message = "170900170900"

#Sets up the socket
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) #Udp

#Sends the data
sock.sendto(bytes(message, "utf-8"), (targetIP, targetPort))
