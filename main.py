from games.tictactoe import TicTacToe

if __name__ == "__main__":
    size = int(input("Enter the size of the board you want to play on: "))
    piece_zero = input("Player zero, enter the piece you want to play with (any one character): ")
    piece_one = input("Player one, enter the piece you want to play with: ")
    game = TicTacToe(piece_zero, piece_one, size)

    while not game.check_win():
        game.print_board()

        pos = input(f"Player {game.current}'s turn: ")
        pos = tuple(map(int, pos.split(" ")))

        print(game.make_move(pos))
    
    game.print_board()
    print(f"Player {game.current} wins!")
        