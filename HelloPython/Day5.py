"""
Day 5 — Nested Lists
Problem: Create a 3x3 matrix (a list of lists) representing a tic-tac-toe board filled with ".".

Print the board in a grid format.
Place "X" at row 0, col 1 and "O" at row 2, col 2.
Print the updated board.
Write a function get_row(board, row) that returns all elements in a given row.
Write a function get_col(board, col) that returns all elements in a given column.
Concepts: Nested lists, indexing with [i][j], functions
"""
from typing import Any

# Function to create list of lists
def create_board(rows, col):
    board_list: list[Any] = []
    for _ in range(rows):
        row = ["."] * col
        board_list.append(row)
    return board_list

# print(create_board(3,3))
my_game_board = create_board(3, 3)

#Print the board in a grid format
def board_in_matrix():
    for row in my_game_board:
        print(row)

# Place "X" at row 0, col 1 and "O" at row 2, col 2.
my_game_board[0][1] = "X"
my_game_board[1][1] = "O"

# Print the updated board
board_in_matrix()

# Write a function get_row(board, row) that returns all elements in a given row.
def get_row(board, row_index):
    return board[row_index]

get_row_zero = get_row(my_game_board, 2)
print(get_row_zero)

# Write a function get_col(board, col) that returns all elements in a given column.
def get_col(board, col_index):
    return [row[col_index] for row in board]

get_col_zero = get_col(my_game_board, 2)
print(get_col_zero)
