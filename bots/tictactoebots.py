import copy
import random
class TripleTeeBot():
    def __init__(self, diff_level):
        self.level = diff_level

    def select(self, game):
        moves = game.available_moves()
        winner = game.winning_move(moves)

        if self.level == 0:
            if not winner: return random.choice(moves)
            return winner
        
        
        
        

