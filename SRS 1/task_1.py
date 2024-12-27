def print_board(brd):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {brd[i]} | {brd[i+1]} | {brd[i+2]} ")
        if i < 6:
            print("---+---+---")
    print("\n")

def check_winner(brd, symbol):
    patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for pattern in patterns:
        if all(brd[i] == symbol for i in pattern):
            return True
    return False

def is_draw(brd):
    return all(isinstance(x, str) for x in brd)

def player_move(brd):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or not isinstance(brd[move], int):
                print("Invalid move! Try again.")
            else:
                brd[move] = 'X'
                break
        except ValueError:
            print("Please enter a number between 1 and 9.")

def computer_move(brd):
    for i in range(9):
        if isinstance(brd[i], int):
            brd[i] = 'O'
            if check_winner(brd, 'O'):
                return
            brd[i] = i + 1
    for i in range(9):
        if isinstance(brd[i], int):
            brd[i] = 'X'
            if check_winner(brd, 'X'):
                brd[i] = 'O'
                return
            brd[i] = i + 1
    if isinstance(brd[4], int):
        brd[4] = 'O'
        return
    corners = [0, 2, 6, 8]
    for c in corners:
        if isinstance(brd[c], int):
            brd[c] = 'O'
            return
    sides = [1, 3, 5, 7]
    for s in sides:
        if isinstance(brd[s], int):
            brd[s] = 'O'
            return

def main():
    while True:
        board = [i + 1 for i in range(9)]
        print("Welcome to Tic-Tac-Toe!")
        print_board(board)
        while True:
            player_move(board)
            print_board(board)
            if check_winner(board, 'X'):
                print("Congratulations! You win!")
                break
            if is_draw(board):
                print("It's a draw!")
                break
            computer_move(board)
            print_board(board)
            if check_winner(board, 'O'):
                print("Computer wins! Better luck next time.")
                break
            if is_draw(board):
                print("It's a draw!")
                break
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()