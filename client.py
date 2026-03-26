import socket
import time

bufferSize = 1024

#socket creation
UDPClientSocket=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 

serverAddressPort   = ("127.0.0.1", 20001)

#sending T1
T1 = time.time()  #gets current time of system clock
msg = str(T1)
bytesToSend = str.encode(msg)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

#Receiving T2 and T3
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg1 = (msgFromServer[0]).decode()
T2 = float(msg1)

msgFromServer1 = UDPClientSocket.recvfrom(bufferSize)
msg2 = (msgFromServer1[0]).decode()
T3 = float(msg2)

T4 = time.time()

delay = (T4 - T1) - (T3 - T2)
offset = ((T2 - T1) + (T3 - T4)) / 2

print("T1:",T1)
print("T2:",T2)
print("T3:",T3)
print("T4:",T4)
print("Delay: ",delay)
print("Offset: ",offset)

UDPClientSocket.close()