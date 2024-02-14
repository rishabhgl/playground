class TicTacToe():

    def __init__(self, piece_one = "O", piece_two = "X", size = 3):
        self.size = size
        self.board = [[" "] * size for i in range(size)]
        self.player_pieces = (piece_one, piece_two)
        self.current = 1

    def check_win(self):

        sum_rows = [0] * self.size
        sum_cols = [0] * self.size
        sum_diagonals = [0, 0]

        for i in range(self.size):
            for j in range(self.size):  
                if self.board[i][j] == self.player_pieces[self.current]:
                    sum_rows[i] += 1
                    sum_cols[j] += 1
                    if i == j:
                        sum_diagonals[0] += 1
                    if j == self.size - 1 - i:
                        sum_diagonals[1] += 1

        if sum_diagonals[0] == self.size or sum_diagonals[1] == self.size:
            return True
        
        for i in range(self.size):
            if sum_cols[i] == self.size or sum_rows[i] == self.size:
                return True

        self.current = (self.current + 1) % 2
        return False

    def make_move(self, pos):

        out_of_bounds = pos[0] >= self.size or pos[0] < 0 or pos[1] >= self.size or pos[1] < 0
        if not out_of_bounds and self.board[pos[0]][pos[1]] == " ":
            self.board[pos[0]][pos[1]] = self.player_pieces[self.current]
            return ""
        else:
            self.current = (self.current + 1) % 2
            return "Invalid move! Try again~"
            
    def print_board(self):
        border = "---" * self.size
        for i in range(self.size):
            print(border)
            for j in range(self.size):
                print(f"|{self.board[i][j]}|", end = "")
            print("")
            print(border)
    