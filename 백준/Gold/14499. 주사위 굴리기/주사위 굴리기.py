import sys
from collections import deque
input = sys.stdin.readline

N,M,y,x,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
orders = list(map(int,input().split()))
dice = deque([0,0,0,0,0,0])
side = [0,4,2,5]
def dice_front(n):
    tmp = dice[3]
    if n == 3:
        for i in range(3):
            dice[i],dice[(i+1)%4] = dice[(i+1)%4],dice[i]
    else:
        del dice[3]
        dice.appendleft(tmp)
    return dice[0]
def dice_side(n):
    for i in range(3):
        dice[side[i]],dice[side[(i+1)%4]] = dice[side[(i+1)%4]],dice[side[i]]
    if n == 2:
        dice[0],dice[2] = dice[2],dice[0]
        dice[4],dice[5] = dice[5],dice[4]
    return dice[0]

for order in orders:
    if order == 1:
        if x+1 < M and x+1 > -1 and y < N and y > -1:
            x+=1
            tmp = dice_side(1)
            if board[y][x] == 0:
                board[y][x] = tmp
            else:
                dice[0] = board[y][x]
                board[y][x] = 0
            print(dice[2])
    elif order == 2:
        if x-1 < M and x-1 > -1 and y < N and y > -1:
            x-=1
            tmp = dice_side(2)
            if board[y][x] == 0:
                board[y][x] = tmp
            else:
                dice[0] = board[y][x]
                board[y][x] = 0
            print(dice[2])
    elif order == 3:
        if x < M and x > -1 and y-1 < N and y-1 > -1:
            y-=1
            tmp = dice_front(3)
            if board[y][x] == 0:
                board[y][x] = tmp
            else:
                dice[0] = board[y][x]
                board[y][x] = 0
            print(dice[2])
    elif order == 4:
        if x < M and x > -1 and y+1 < N and y+1 > -1:
            y+=1
            tmp = dice_front(4)
            if board[y][x] == 0:
                board[y][x] = tmp
            else:
                dice[0] = board[y][x]
                board[y][x] = 0
            print(dice[2])