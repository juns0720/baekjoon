import sys
input = sys.stdin.readline

n = int(input())
command = list(input().strip())
dir = {'D': (1,0), 'U': (-1,0), 'R': (0,1), 'L': (0,-1)}

board = [['.' for _ in range(n)] for _ in range(n)]

y,x = 0,0

def check(y,x,c):
    if c in ['U','D']:
        if  board[y][x] == '.':
            board[y][x] = '|'
        elif board[y][x] == '-':
            board[y][x] = '+'
    else:
        if board[y][x] == '.':
            board[y][x] = '-'
        elif board[y][x] == '|':
            board[y][x] = '+'


for crnt in command:
    ny,nx = y + dir[crnt][0], x + dir[crnt][1]
    if ny < 0 or ny > n-1 or nx < 0 or nx > n-1:
        continue
    check(y,x,crnt)
    y,x = ny,nx
    check(y,x,crnt)


for i in board:
    for j in i:
        print(j,end='')
    print()