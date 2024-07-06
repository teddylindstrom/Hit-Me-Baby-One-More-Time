import random

# Game board size#
def print_board(board):
    for row in board:
        print(" ".join(row))

# The size of the board, rows, columns#
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

    #placement of the ship
    else:
        row = random.randint(0, len(board) - ship_length)
        col = random.randint(0, len(board) - 1)
        for i in range(ship_length):
            board[row + i][col] = "S"
    return board


"""
    Check if a guessed position is valid on the game board.

    Args:
        board (list of list): The game board represented as a 2D list.
        row (int): The guessed row index.
        col (int): The guessed column index.

    Returns:
        bool: True if the guessed position is valid (within board boundaries), False otherwise.
    """
def is_valid_guess(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0])

def main():
    """
    Main function to initialize and run the battleship game.

    Initializes game parameters such as board size, ship length, and number of attempts.
    Creates the game board and hidden board using the create_board function.
    Places a ship of specified length on the board using the place_ship function.
    """
    size = 5 # Size of the game board (5x5 grid)
    ship_length = 3 # Length of the ship to be placed on the board
    attempts = 10 # Number of attempts allowed to guess the ship's location

    # Create the game board and hidden board
    board = create_board(size)
    hidden_board = create_board(size)

    # Place a ship of specified length on the game board
    board = place_ship(board, ship_length)

    # Display welcome message and game instructions
    print("Welcome to 'Hit Me Baby One More Time' Battleship Game!")
    print(f"You have {attempts} attempts to sink the ship!")

    while attempts > 0:
        # Display the current game board for the player to see
        print("\nCurrent Board:")
        print_board(hidden_board)

         # Get player's guess for row and column
        guess_row = int(input("Guess Row (0-4): "))
        guess_col = int(input("Guess Col (0-4): "))

        # Validate if the guessed position is within the board boundaries
        if not is_valid_guess(hidden_board, guess_row, guess_col):
            print("Invalid guess. Please enter numbers between 0 and 4.")
            continue
        
        # Check if the player has already guessed the spot
        if hidden_board[guess_row][guess_col] in ["X", "H"]:
            print("You already guessed that spot.")
            continue
        
        # Check if the guess hit a ship
        if board[guess_row][guess_col] == "S":
            print("Hit!")
            hidden_board[guess_row][guess_col] = "H"
            board[guess_row][guess_col] = "H"

            # Check if all parts of the ship have been hit
            if all(board[row][col] != "S" for row in range(size) for col in range(size)):
                print("Congratulations! You've sunk the ship!")
                print_board(hidden_board)
                return
        else:
            print("Miss!")
            hidden_board[guess_row][guess_col] = "X"

        # Decrease the attempts count after each guess
        attempts -= 1

        # Check if the game is over due to no remaining attempts
        if attempts == 0:
            print("Game Over! You've run out of attempts.")
        else:
            print(f"Remaining attempts: {attempts}")
        
        
    # Display the final state of the game board with all guesses revealed
    print("Final Board:")
    print_board(hidden_board)

    # Display the actual locations of the ship on the board
    print("The ship was at:")
    print_board(board)

# Check if this script is being run directly as the main program
if __name__ == "__main__":
    main()