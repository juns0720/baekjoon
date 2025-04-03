import sys
from copy import deepcopy
input = sys.stdin.readline

n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
query = [list(map(int,input().split())) for _ in range(k)]

def rotate(board,sy,sx,ey,ex):
    tmp = board[sy][ex]
    #UP
    for x in range(ex,sx,-1):
        board[sy][x] = board[sy][x-1]
    
    #LEFT
    for y in range(sy,ey):
        board[y][sx] = board[y+1][sx]
    #DOWN
    for x in range(sx,ex):
        board[ey][x] = board[ey][x+1]
    #RIGHT
    for y in range(ey,sy,-1):
        board[y][ex] = board[y-1][ex]
    board[sy+1][ex] = tmp

    return board

def cal_query(board,sy,sx,ey,ex):
    while sx < ex and sy < ey:
        board = rotate(board,sy,sx,ey,ex)
        sy += 1
        sx += 1
        ey -= 1
        ex -= 1
    return board


def recursion(depth, crnt_board):
    global res
    if depth == k:
        res = min(res,cal_res(crnt_board))
        return
    
    for i in range(k):
        if visited[i]:
            continue
        r,c,s = query[i]
        sy,sx = r-s-1,c-s-1
        ey,ex = r+s-1,c+s-1
        
        visited[i] = 1
        recursion(depth+1,deepcopy(cal_query(deepcopy(crnt_board),sy,sx,ey,ex)))
        visited[i] = 0


def cal_res(board):
    min_res = sys.maxsize
    for r in range(n):
        min_res = min(min_res, sum(board[r]))
    return min_res

visited = [0 for _ in range(k)]
res = sys.maxsize
recursion(0,deepcopy(board))
print(res)