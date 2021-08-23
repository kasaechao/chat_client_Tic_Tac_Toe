# Name: Kao Saechao
# Date: 08/06/2021
# Description: Programming Project 4

from socket import *
from TicTacToe import *
from random import *
import pickle

serverPort = 1024  # specify connection port
serverSocket = socket(AF_INET, SOCK_STREAM)  # create server socket
host = '127.0.0.1'
serverSocket.bind((host, serverPort))  # establish the welcoming connection
serverSocket.listen(1)  # listen for a client socket, specifying 1 max number of queued connections
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
connectionSocket, addr = serverSocket.accept()  # create a new socket when a client requests a connection

print(f"Server listening on: localhost on port: {serverPort}")
print(f"connected to: {addr[0]} on port {serverPort}")
print("Waiting for message...")
move = connectionSocket.recv(1024).decode()
print(f"client reply: {move}")
connectionSocket.send(
    "Hi there, lets play Tic Tac Toe. Enter a number between (1-9) inclusive, '/q' to quit anytime.".encode())

# Tic Tac Toe game instance
# game = TicTacToe()
# x = game.x_player
# o = game.o_player
# board = game.board

game = TicTacToe()
x = game.x_player
o = game.o_player
board = game.board

while True:
    if not move:
        break

    # server will randomly make moves
    if game.get_turn() == 'o':
        # check for a winning condition
        if game.check_winner(board.get_board()) != None:
            send_board = pickle.dumps(game.get_board())
            connectionSocket.send(send_board)
            connectionSocket.send(f"GAME OVER, {game.get_winner()} won!".encode())
            game.print_board()
            print("GAME OVER")
            break
        else:
            move = randint(1, 9)
            # move = game.convert_player_input(move)
            is_valid = game.is_valid_move(move)
            while not is_valid:
                move = randint(1, 9)
                is_valid = game.is_valid_move(move)

            move = game.convert_player_input(move)
            board.set_board(move, game.get_turn())
            game.set_turn()

            send_board = pickle.dumps(game.get_board())
            connectionSocket.send(send_board)
            game.print_board()

    # if x turn then server will ask the client to make a move
    else:
        # exception handling for when the client quits
        try:
            move = int(connectionSocket.recv(1024))
        except:
            print("The client has disconnected....")
            break

        if game.check_winner(board.get_board()) != None:
            game.print_board()
            connectionSocket.send(f"GAME OVER, {game.get_winner()} won!".encode())
            print("AI WINS!")
            break

        if not game.is_valid_move(move):
            connectionSocket.send("Move invalid, Enter a number between (1-9) inclusive: ".encode())

        move = game.convert_player_input(move)
        board.set_board(move, game.get_turn())
        game.set_turn()

connectionSocket.send("Thanks for playing, bye! '/q' to diconnect".encode())
try:
    data = connectionSocket.recv(1024).decode()
    if not data:
        keep_playing = False
except:
    print("The client has disconnected....")

connectionSocket.close()
