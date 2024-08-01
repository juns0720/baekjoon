import sys
sys.setrecursionlimit(100)
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(9)]



def check(row,col,num):
    #가로
    if num in board[row]:
        return False
    #세로
    for cur_row in range(9):
        if num == board[cur_row][col]:
            return False
    #3x3

    s_row = (row // 3) * 3
    s_col = (col // 3) * 3
    for row2 in range(s_row,s_row+3):
        for col2 in range(s_col, s_col+3):
            if board[row2][col2] == num:
                return False
    return True

def sudoku(row,col):
    if col == 9:
        row += 1
        col = 0
    if row == 9:
        for tmp in board:
            for num in tmp:
                print(num,end='')
            print()
        exit()

    if board[row][col] == '0':
        for num in range(1,10):
            if check(row,col,str(num)):
                board[row][col] = str(num)
                sudoku(row,col+1)
                board[row][col] = '0'
    else:
        sudoku(row,col+1)
sudoku(0,0)
