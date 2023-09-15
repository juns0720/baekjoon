import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
def find_shark():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                return (i,j)
    return (-1,-1)

food = []
lev = [2,0]
dis = 0
def BFS(sy,sx):
    dy = [-1,0,1,0]
    dx = [0,-1,0,1]
    ay,ax = sy,sx
    while queue:
        y,x,d = queue.popleft()
        for i in range(4):
            ty = y+dy[i]
            tx = x+dx[i]
            if -1 < ty < N and -1 < tx < N and not visited[ty][tx]:
                if board[ty][tx] != 0 and -1 < board[ty][tx] < lev[0]:
                    food.append([ty,tx,d+1])
                elif board[ty][tx] == 0 or board[ty][tx] == lev[0]:
                    visited[ty][tx] = 1
                    queue.append((ty,tx,d+1))
    if food:
        food.sort(key = lambda x : (x[2],x[0]))
        ay,ax,d = food[0][0],food[0][1],food[0][2]
        board[ay][ax] = 9
        lev[1]+=1
        if lev[0] == lev[1]:
            lev[0]+=1
            lev[1] = 0
        queue.clear()
        food.clear()
        return d
    else:
        d = 0
        return d
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque([])
    y,x = find_shark()
    if y == -1 and x == -1:
        break
    queue.append((y,x,0))
    visited[y][x] = 1
    board[y][x] = 0
    dis += BFS(y,x)
print(dis)