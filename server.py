import socket
import time

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

# socket creation
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))  #binds the server socket to IP address and Port Number 

print("UDP server up and listening")

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    # Decode client message (T1)
    client_time = message.decode()
    print("Message from Client:", client_time)
    print("Client Address:", address)

    # Record timestamps
    T2 = time.time()   # time request received
    T3 = time.time()   # time reply sent

    bytesT2 = str(T2).encode()
    bytesT3 = str(T3).encode()

    # Send T2 and T3
    UDPServerSocket.sendto(bytesT2, address)
    UDPServerSocket.sendto(bytesT3, address)

    print("T2:", T2)
    print("T3:", T3)