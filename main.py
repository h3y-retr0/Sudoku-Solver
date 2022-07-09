

default_board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def print_board(board):
    for i_row, row in enumerate(board):
        if i_row % 3 == 0:
            print("------------------------")
        board_row = ''
        for i_elem, elem in enumerate(row):
            if elem == 0:
                elem = ' '
            if i_elem % 3 == 0:
                board_row += '| ' + str(elem) + ' '
            elif i_elem == 8:
                board_row += str(elem) + ' |'
            else:
                board_row += str(elem) + ' '
        print(board_row)
        if i_row == 8:
            print('------------------------')

# print_board(default_board)

def find_zero(board):
    # Returns the first 0 position as an array [row, column]
    # If there is no 0, returns an empty list
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                return [r, c]
    return []

find_zero(default_board)
def solve(board):
    return

