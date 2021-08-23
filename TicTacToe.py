class TicTacToe:
    """
    class of a Tic Tac Toe Game
    """

    def __init__(self):
        self.x_player = Player('x')
        self.o_player = Player('o')
        self.board = Board()
        self.turn = 'x'
        self.winner = None  # will be used to determine winner

    def get_winner(self):
        """get winner of the game"""
        return self.winner

    def get_board(self):
        """get the board"""
        return self.board.get_board()

    def check_winner(self, board):
        """ check if there is a winner """
        # horizontal wins ---------------------------------------------------------
        if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
            self.winner = 'x'
        elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
            self.winner = 'x'
        elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
            self.winner = 'x'
        elif board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
            self.winner = 'o'
        elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
            self.winner = 'o'
        elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
            self.winner = 'o'

        # vertical wins -----------------------------------------------------------
        elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
            self.winner = 'x'
        elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
            self.winner = 'x'
        elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
            self.winner = 'x'
        elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
            self.winner = 'o'
        elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
            self.winner = 'o'
        elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
            self.winner = 'o'

        # diagonal wins -----------------------------------------------------------
        elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
            self.winner = 'x'
        elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
            self.winner = 'x'
        elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
            self.winner = 'o'
        elif board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
            self.winner = 'o'

        return self.winner

    def get_turn(self):
        """ get the current turn in the game """
        return self.turn

    def set_turn(self):
        """ toggle turn after each player move """
        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'

    def print_board(self):
        """ print the current board state """
        board = self.board.get_board()
        [print(row) for row in board]

    def convert_player_input(self, move_input):
        """ convert the player input to board coordinates"""
        move_input -= 1
        move_converted = (move_input // 3, move_input % 3)
        return move_converted

    def is_valid_move(self, move):
        """determine if the move entered is valid"""
        is_valid = True
        if type(move) != int:
            is_valid = False
            print(move, type(move))
        elif 0 < move < 10:
            move = self.convert_player_input(move)
            row, col = move[0], move[1]
            board = self.board.get_board()

            # if location on board is out of index
            if not board[row][col]:
                is_valid = False
            # if location on board is occupied
            if board[row][col] != "_":
                is_valid = False
        else:
            is_valid = False
        return is_valid


class Player:
    """
    class for players of the game
    """

    def __init__(self, player_piece):
        self.piece = player_piece


class Board:
    """
    class for the game board
    """

    def __init__(self):
        self.board = [["_" for _ in range(3)] for _ in range(3)]

    def get_board(self):
        """return the board"""
        return self.board

    def set_board(self, loc, player):
        """modify the board"""
        row = loc[0]
        col = loc[1]
        self.board[row][col] = player


def main():
    game = TicTacToe()
    x = game.x_player
    o = game.o_player
    board = game.board

    while game.check_winner(board.get_board()) is None:
        move = int(input(f"Player {game.turn}, choose a number between (1-9) inclusive: "))
        while not game.is_valid_move(move):
            move = int(input(f"move invalid, choose a number between (1-9) inclusive: "))

        move = game.convert_player_input(move)
        board.set_board(move, game.get_turn())
        game.print_board()
        game.set_turn()
    print(f"GAME OVER, {game.get_winner()} won!")


if __name__ == '__main__':
    main()
