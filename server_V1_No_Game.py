# Name: Kao Saechao
# Date: 08/06/2021
# Description: Programming Project 4
import socket
from socket import *

serverPort = 1024   # specify connection port
serverSocket = socket(AF_INET, SOCK_STREAM)     # create server socket
host = '127.0.0.1'
serverSocket.bind((host, serverPort))     # establish the welcoming connection
serverSocket.listen(1)      # listen for a client socket, specifying 1 max number of queued connections
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
connectionSocket, addr = serverSocket.accept()  # create a new socket when a client requests a connection

print(f"Server listening on: localhost on port: {serverPort}")
print(f"connected to: {addr[0]} on port {serverPort}")
print("Waiting for message...")
inData = connectionSocket.recv(1024)

while True:
    inData = connectionSocket.recv(1024).decode()
    if not inData:
        break
    print(f"From client: {inData}")
    outData = input("Enter your message: ")
    connectionSocket.send(outData.encode())

connectionSocket.close()


