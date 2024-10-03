# Design 8-Queens matrix having first Queen placed. Use backtracking to place remaining Queens to generate the final 8-queen’s matrix.

# Function to check if a queen can be placed on board[row][col]
def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Backtracking function to solve the 8-Queens problem
def solve_queens(board, col):
    # If all queens are placed, return True
    if col >= len(board):
        return True

    # Consider this column and try placing a queen in each row
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_queens(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If no placement is possible in this column, return False
    return False

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))

# Initialize an 8x8 chessboard
def solve_8_queens():
    N = 8
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Place the first queen manually (say at position (0, 0))
    board[0][0] = 1

    # Solve for the remaining queens starting from column 1
    if solve_queens(board, 1):
        print_board(board)
    else:
        print("No solution exists.")

# Execute the function
solve_8_queens()