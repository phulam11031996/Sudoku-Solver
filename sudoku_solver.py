import math
import os
import time



board = [[6,0,0,5,2,0,4,0,0],
        [0,5,3,0,1,0,6,8,7],
        [0,1,4,0,6,7,0,0,2],
        [0,6,0,0,0,2,8,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,2,1,0,0,0,3,0],
        [5,0,0,7,4,0,1,9,0],
        [1,3,9,0,5,0,7,4,0],
        [0,0,7,0,3,1,0,0,5],]

board1 =   [[0,0,0,0,0,2,0,7,0],
            [0,0,8,0,0,0,0,0,0],
            [0,5,0,1,0,6,0,0,2],
            [0,2,0,0,0,0,4,0,5],
            [6,0,9,0,0,7,0,0,0],
            [0,0,0,9,8,0,0,2,0],
            [0,0,0,0,0,8,0,0,4],
            [1,0,5,0,0,0,6,0,0],
            [0,0,0,0,6,0,0,0,9],]



def print_board(board):
    for row in range(len(board)):
        if row == 3 or row == 6:
            print('- - - - - - - - - - - - - - - - - -')
        for col in range(len(board)):
            if col == 3 or col == 6:
                print('  |  ' + str(board[row][col]), end='')
            elif col == 8:
                print('  ' + str(board[row][col]))
            else:
                print('  ' + str(board[row][col]), end='')


def empty(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return (row, col)
    return None


def valid(board, number, position):
    # check row
    for index in range(9):
        if board[position[0]][index] == number:
            return False

    # check column
    for index in range(9):
        if board[index][position[1]] == number:
            return False

    # check square
    row = math.floor(position[0]/3)*3
    col = math.floor(position[1]/3)*3
    for row_count in range(3):
        for col_count in range(3):
            if number == board[row+row_count][col+col_count]:
                return False
    return True



def solve(board):
    os.system('cls')
    print_board(board)
    time.sleep(0.2)

    find = empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1,10):
        if valid(board, num, find):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


print('This is the initial board.')
print_board(board)
some_input = input('Press a key to start solving.')
solve(board)

