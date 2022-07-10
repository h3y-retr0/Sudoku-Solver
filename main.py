

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# board = [[0, 8, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 2, 1, 8, 7, 0],
#          [2, 0, 0, 3, 0, 0, 0, 5, 9],
#          [0, 0, 4, 0, 0, 9, 0, 2, 0],
#          [0, 7, 0, 2, 1, 8, 4, 0, 6],
#          [9, 0, 0, 0, 0, 3, 7, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [6, 9, 0, 4, 0, 0, 0, 0, 0],
#          [0, 4, 8, 1, 0, 7, 0, 0, 0]]


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


def check_user_board(board):
    num_row = len(board)
    num_col = len(board[0])

    if num_row == 9 and num_col == 9:
        return True
    else:
        print("Enter a valid board please")
        return False


def find_zero(board):
    # Returns the first 0 position as an array [row, column]
    # If there is no 0, returns an empty list
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                return [r, c]
    return []


def is_valid(board, row, col, value):

    #Row Check
    for i in board[row]:
        if i == value:
            return False

    #Col Check

    for j in range(len(board)):
        if value == board[j][col]:
            return False
    # 3x3 single grid check

    r = (row - (row % 3))
    c = (col - (col % 3))

    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if value == board[i][j]:
                return False

    # Everything Ok.
    return True

def solve(board):

    # Base Case
    nxt_position = find_zero(board)

    if nxt_position == []:
        return board
    
    # Recursion
    row = nxt_position[0]
    col = nxt_position[1]

    for i in range(1, 10):
        if is_valid(board, row, col, i):
            board[row][col] = i
            solution = solve(board)

            if solution is not None:
                return solution

    # Backtrack:

    board[row][col] = 0
    
    # See the recursion process:
    # print_board(board)
    return None


userInput = input('Press enter to start the program: ')

if userInput == "":
    print_board(board)
    check = input('Press enter to solve this sudoku: ')
    if check == "":
        if solve(board):
            print("")
            print("Solution: ")
            print("")
            print_board(solve(board))
            print("")
        else:
            print_board(board)
            print("No solution")            
else:
    exit

