Hit Me Baby One More Time
import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def create_board(size):
    return [["O"] * size for _ in range(size)]

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