"""Sudoku Solver
Given a partially filled two-dimensional array, fill all the unfilled cells such that each row, each column and each 3 x 3 subgrid (as highlighted below by bolder lines) has every digit from 1 to 9 exactly once.

Unfilled cells have a value of 0 on the given board.

Example
Example one

{
"board": [
[8, 4, 9, 0, 0, 3, 5, 7, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[7, 0, 0, 0, 9, 0, 0, 8, 3],
[0, 0, 0, 9, 4, 6, 7, 0, 0],
[0, 8, 0, 0, 5, 0, 0, 4, 0],
[0, 0, 6, 8, 7, 2, 0, 0, 0],
[5, 7, 0, 0, 1, 0, 0, 0, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 2, 1, 7, 0, 0, 8, 6, 5]
]
}
Output:

[
[8, 4, 9, 1, 6, 3, 5, 7, 2],
[3, 1, 5, 2, 8, 7, 4, 9, 6],
[7, 6, 2, 4, 9, 5, 1, 8, 3],
[1, 5, 3, 9, 4, 6, 7, 2, 8],
[2, 8, 7, 3, 5, 1, 6, 4, 9],
[4, 9, 6, 8, 7, 2, 3, 5, 1],
[5, 7, 8, 6, 1, 9, 2, 3, 4],
[6, 3, 4, 5, 2, 8, 9, 1, 7],
[9, 2, 1, 7, 3, 4, 8, 6, 5]
]
Notes
You can assume that any given puzzle will have exactly one solution.

Constraints:

Size of the input array is exactly 9 x 9
0 <= value in the input array <= 9"""


def solve_sudoku_puzzle(board):
    def is_safe(row, col, num):
        for i in range(9):
            if num == board[row][i] or num == board[i][col]:
                return False
        quad_row_start = row - row % 3
        quad_col_start = col - col % 3
        for i in range(quad_row_start, quad_row_start + 3):
            for j in range(quad_col_start, quad_col_start + 3):
                if board[i][j] == num:
                    return False
        return True

    def next_unsolved():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j

    def helper():
        pair = next_unsolved()
        if not pair:
            # Done all full
            return True
        i, j = pair
        for num in range(1, 10):
            if is_safe(i, j, num):
                board[i][j] = num
                if helper():
                    return True
                else:
                    board[i][j] = 0
        return False

    helper()
    return board


board = solve_sudoku_puzzle(
    [
        [8, 4, 9, 0, 0, 3, 5, 7, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 9, 0, 0, 8, 3],
        [0, 0, 0, 9, 4, 6, 7, 0, 0],
        [0, 8, 0, 0, 5, 0, 0, 4, 0],
        [0, 0, 6, 8, 7, 2, 0, 0, 0],
        [5, 7, 0, 0, 1, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 2, 1, 7, 0, 0, 8, 6, 5],
    ]
)
for row in board:
    print(" ".join([str(val) for val in row]))
