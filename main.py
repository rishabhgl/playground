from games.game import TicTacToe

if __name__ == "__main__":

    game = TicTacToe()

    while not game.check_win():
        game.print_board()

        pos = input(f"Player {game.current}'s turn: ")
        pos = tuple(map(int, pos.split(" ")))

        print(game.make_move(pos))
    
    game.print_board()
    print(f"Player {game.current} wins!")
        