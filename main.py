import random

#Game board size#
def print_board(board):
    for row in board:
        print(" ".join(row))

#The size of the board, rows, columns#
def create_board(size):
    return [["O"] * size for _ in range(size)]


    """
    Randomly places a ship on the game board.

    Args:
        board (list of list of str): The game board represented as a 2D list.
        ship_length (int): The length of the ship to be placed.

    Returns:
        list of list of str: The updated game board with the ship placed.
    """
def place_ship(board, ship_length):
    direction = random.choice(["H", "V"])
    if direction == "H":
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board) - ship_length)
        for i in range(ship_length):
            board[row][col + i] = "S"

    else:
        row = random.randint(0, len(board) - ship_length)
        col = random.randint(0, len(board) - 1)
        for i in range(ship_length):
            board[row + i][col] = "S"
    return board

def is_valid_guess(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0])

def main():
    size = 5
    ship_length = 3
    attempts = 10

    board = create_board(size)
    hidden_board = create_board(size)
    board = place_ship(board, ship_length)

    print("Welcome to 'Hit Me Baby One More Time' Battleship Game!")
    print(f"You have {attempts} attempts to sink the ship!")

    while attempts > 0:
        print("\nCurrent Board:")
        print_board(hidden_board)
        guess_row = int(input("Guess Row (0-4): "))
        guess_col = int(input("Guess Col (0-4): "))

        if not is_valid_guess(hidden_board, guess_row, guess_col):
            print("Invalid guess. Please enter numbers between 0 and 4.")
            continue
        if hidden_board[guess_row][guess_col] in ["X", "H"]:
            print("You already guessed that spot.")
            continue
        if board[guess_row][guess_col] == "S":
            print("Hit!")
            hidden_board[guess_row][guess_col] = "H"
            board[guess_row][guess_col] = "H"
            if all(board[row][col] != "S" for row in range(size) for col in range(size)):
                print("Congratulations! You've sunk the ship!")
                print_board(hidden_board)
                return
        else:
            print("Miss!")
            hidden_board[guess_row][guess_col] = "X"
        attempts -= 1
        if attempts == 0:
            print("Game Over! You've run out of attempts.")
        else:
            print(f"Remaining attempts: {attempts}")
        
        
    
    print("Final Board:")
    print_board(hidden_board)
    print("The ship was at:")
    print_board(board)

if __name__ == "__main__":
    main()