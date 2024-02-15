import copy

class TicTacToe():

    def __init__(self, piece_one = "O", piece_two = "X", size = 3):
        self.size = size
        self.board = [[" "] * size for i in range(size)]
        self.player_pieces = (piece_one, piece_two)
        self.current = 0
        self.prev = 1
        self.move_count = 0


    def change_player(self, restore = False):
        if restore:
            self.current = restore
            self.prev = (self.current + 1) % 2
            return
        
        self.prev = self.current
        self.current = (self.current + 1) % 2

        
    def check_win(self, simulation = False):
        player = self.prev
        
        if simulation:
            player = self.current
        
        sum_rows = [0] * self.size
        sum_cols = [0] * self.size
        sum_diagonals = [0, 0]

        for i in range(self.size):
            for j in range(self.size):  
                if self.board[i][j] == self.player_pieces[player]:
                    sum_rows[i] += 1
                    sum_cols[j] += 1
                    if i == j:
                        sum_diagonals[0] += 1
                    if j == self.size - 1 - i:
                        sum_diagonals[1] += 1

        if sum_diagonals[0] == self.size or sum_diagonals[1] == self.size:
            if not simulation: print(f"Player {player} wins!")
            return True
        
        for i in range(self.size):
            if sum_cols[i] == self.size or sum_rows[i] == self.size:
                if not simulation: print(f"Player {player} wins!")
                return True
            
        if self.is_full():
            if not simulation: print("The game is a tie!")
            return True
        
        return False
    

    def is_full(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == " ":
                    return False

        return True


    def make_move(self, pos, simulation = False):

        out_of_bounds = pos[0] >= self.size or pos[0] < 0 or pos[1] >= self.size or pos[1] < 0
        if not out_of_bounds and self.board[pos[0]][pos[1]] == " ":
            self.board[pos[0]][pos[1]] = self.player_pieces[self.current]
            if not simulation:
                self.move_count += 1
                self.change_player()
            return ""
        else:
            return "Invalid move! Try again~"
        

    def winning_move(self, moves):

        BOARD = self.board

        for move in moves:
            state = copy.deepcopy(BOARD)
            self.board = state
            self.make_move(move, simulation= True)
            if self.check_win(simulation=True):
                self.board = BOARD
                return move
            self.board = BOARD

        return False
    

    def block_opponent(self, moves):
        BOARD = self.board
        CURRENT = self.current

        for move in moves:
            state = copy.deepcopy(BOARD)
            self.board = state
            self.make_move(move, simulation= True)
            self.change_player()
            opp_moves = self.available_moves()
            opp_win = self.winning_move(opp_moves)
            if opp_win:
                moves = [new_move for new_move in moves if new_move is not move]
            self.change_player(restore = CURRENT)
            self.board = BOARD

        return moves
        

    def available_moves(self):
        moves = []

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == " ":
                    moves += [(i, j)]

        return moves
            

    def print_board(self):
        border = "---" * self.size
        for i in range(self.size):
            print(border)
            for j in range(self.size):
                print(f"|{self.board[i][j]}|", end = "")
            print("")
            print(border)
    