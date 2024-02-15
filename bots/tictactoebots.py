import random

class TripleTeeBot():
    def __init__(self, diff_level):
        self.level = diff_level

    def select(self, game):
        moves = game.available_moves()
        winner = game.winning_move(moves)
        if winner: return winner

        if self.level == 0:
            return random.choice(moves)
        elif self.level == 1:
            smart_moves = game.block_opponent(moves)
            if not smart_moves: return random.choice(moves)
            return random.choice(smart_moves)
        elif self.level == 2:
            pass
    
        
        

