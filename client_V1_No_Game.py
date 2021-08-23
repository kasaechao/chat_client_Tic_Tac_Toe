# Name: Kao Saechao
# Date: 08/06/2021
# Description: Programming Project 4

from socket import *

serverName = '127.0.0.1'   # host name of server to connect
serverPort = 1024     # port number for connection
clientSocket = socket(AF_INET, SOCK_STREAM)     # create socket
clientSocket.connect((serverName, serverPort))  # establish connection between client and server

print(f"Connected to: localhost on port: {serverPort}")
print("say hi to your new friend!")
msg = input("Enter your message: ")
clientSocket.send(msg.encode())

while msg.lower().strip() != "/q":
    clientSocket.send(msg.encode())
    data = clientSocket.recv(1024).decode()
    print("Server Response: " + data)
    msg = input("Enter your message: ")

clientSocket.close()


