# Name: Kao Saechao
# Date: 08/06/2021
# Description: Programming Project 4

from socket import *
import pickle

serverName = '127.0.0.1'   # host name of server to connect
serverPort = 1024     # port number for connection
clientSocket = socket(AF_INET, SOCK_STREAM)     # create socket
clientSocket.connect((serverName, serverPort))  # establish connection between client and server

print(f"Connected to: localhost on port: {serverPort}")
print("say hi to your new friend!")
msg = input("Enter your message:")
clientSocket.send(msg.encode())
data = clientSocket.recv(1024)
print("Server Response: " + data.decode() + "\n")
msg = input("Enter your message:")
clientSocket.send(msg.encode())

while msg.lower().strip() != "/q":

    data = clientSocket.recv(1024)
    if data:
        try:
            data = pickle.loads(data)
            print("Server response: ")
            [print(row) for row in data]
        except:
            data = data.decode()
            print("Server Response: " + data)

    msg = input("\nEnter your message: ")
    clientSocket.send(msg.encode())

clientSocket.close()


