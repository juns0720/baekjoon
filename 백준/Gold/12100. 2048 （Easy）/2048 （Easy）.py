import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
res = 0
def up_combine(board):
    for c in range(n):
        tmp = deque([])
        for r in range(n):
            if board[r][c] != 0:
                tmp.append((r,c))
            
            if len(tmp) == 2:
                if board[tmp[0][0]][tmp[0][1]] != board[tmp[1][0]][tmp[1][1]]:
                    tmp.popleft()
                    continue
                board[tmp[0][0]][tmp[0][1]], board[tmp[1][0]][tmp[1][1]] = board[tmp[0][0]][tmp[0][1]]*2, 0
                tmp.clear()
    return board

def down_combine(board):
    for c in range(n):
        tmp = deque([])
        for r in range(n-1,-1,-1):
            if board[r][c] != 0:
                tmp.append((r,c))
            
            if len(tmp) == 2:
                if board[tmp[0][0]][tmp[0][1]] != board[tmp[1][0]][tmp[1][1]]:
                    tmp.popleft()
                    continue
                board[tmp[0][0]][tmp[0][1]], board[tmp[1][0]][tmp[1][1]] = board[tmp[0][0]][tmp[0][1]]*2, 0
                tmp.clear()
    return board

def left_combine(board):
    for r in range(n):
        tmp = deque([])
        for c in range(n):
            if board[r][c] != 0:
                tmp.append((r,c))
            
            if len(tmp) == 2:
                if board[tmp[0][0]][tmp[0][1]] != board[tmp[1][0]][tmp[1][1]]:
                    tmp.popleft()
                    continue
                board[tmp[0][0]][tmp[0][1]], board[tmp[1][0]][tmp[1][1]] = board[tmp[0][0]][tmp[0][1]]*2, 0
                tmp.clear()
    return board

def right_combine(board):
    for r in range(n):
        tmp = deque([])
        for c in range(n-1,-1,-1):
            if board[r][c] != 0:
                tmp.append((r,c))
            
            if len(tmp) == 2:
                if board[tmp[0][0]][tmp[0][1]] != board[tmp[1][0]][tmp[1][1]]:
                    tmp.popleft()
                    continue
                board[tmp[0][0]][tmp[0][1]], board[tmp[1][0]][tmp[1][1]] = board[tmp[0][0]][tmp[0][1]]*2, 0
                tmp.clear()                
    return board

def up_move(board):
    for c in range(n):
        for r in range(n):
            if board[r][c] != 0:
                mr = r
                for r2 in range(r-1,-1,-1):
                    if board[r2][c] == 0:
                        mr = r2
                board[r][c],board[mr][c] = board[mr][c], board[r][c]
    return board

def down_move(board):
    for c in range(n):
        for r in range(n-1,-1,-1):
            if board[r][c] != 0:
                mr = r
                for r2 in range(r+1,n):
                    if board[r2][c] == 0:
                        mr = r2
                board[r][c],board[mr][c] = board[mr][c], board[r][c]
    return board

def left_move(board):
    for r in range(n):
        for c in range(n):
            if board[r][c] != 0:
                mc = c
                for c2 in range(c-1,-1,-1):
                    if board[r][c2] == 0:
                        mc = c2
                board[r][c],board[r][mc] = board[r][mc], board[r][c]
    return board

def right_move(board):
    for r in range(n):
        for c in range(n-1, -1, -1):
            if board[r][c] != 0:
                mc = c
                for c2 in range(c+1,n):
                    if board[r][c2] == 0:
                        mc = c2
                board[r][c],board[r][mc] = board[r][mc], board[r][c]
    return board

def up(board):
    return up_move(up_combine(up_move(board)))

def down(board):
    return down_move(down_combine(down_move(board)))

def left(board):
    return left_move(left_combine(left_move(board)))

def right(board):
    return right_move(right_combine(right_move(board)))


def game(depth, cur_board):
    global res
    if depth == 5:
        for i in cur_board:
            res = max(res,max(i))
        return
    
    game(depth+1, up(deepcopy(cur_board)))
    game(depth+1, down(deepcopy(cur_board)))
    game(depth+1, right(deepcopy(cur_board)))
    game(depth+1, left(deepcopy(cur_board)))

game(0, board)
print(res)