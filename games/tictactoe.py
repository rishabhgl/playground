class TicTacToe():

    def __init__(self, piece_one = "O", piece_two = "X"):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player_pieces = (piece_one, piece_two)
        self.current = 1

    def check_win(self):

        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][1] and self.board[0][0] != " ":
            return True
        if self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][0] != " ":
            return True
        if self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][0] != " ":
            return True
        if self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[0][0] != " ":
            return True
        if self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[0][1] != " ":
            return True
        if self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[0][2] != " ":
            return True
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[1][1]and self.board[0][0] != " ":
            return True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            return True
        
        self.current = (self.current + 1) % 2
        return False

    def make_move(self, pos):

        if self.board[pos[0]][pos[1]] == " ":
            self.board[pos[0]][pos[1]] = self.player_pieces[self.current]
            return "Good move!"
        else:
            return "Invalid move! Try again"
            
    def print_board(self):
        for i in range(3):
            print("---------")
            for j in range(3):
                print(f"|{self.board[i][j]}|", end = "")
            print("")
            print("---------")
    