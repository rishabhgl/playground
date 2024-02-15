from games.tictactoe import TicTacToe
from utils import prompts
from utils.menus import mode_menu, diff_menu
from bots.tictactoebots import TripleTeeBot

if __name__ == "__main__":

    mode = mode_menu.show()

    if mode == 1:
        diff_level = diff_menu.show()
        bot = TripleTeeBot(diff_level)
        exit()

    size = int(input(prompts.board_size))
    piece_zero = input(prompts.piece_zero)
    piece_one = input(prompts.piece_one)
    game = TicTacToe(piece_zero, piece_one, size)

    while not game.check_win():
        game.print_board()

        pos = input(f"Player {game.current}'s turn: ")
        pos = tuple(map(int, pos.split(" ")))

        result = game.make_move(pos)
        
        print(result)
    
    game.print_board()
        