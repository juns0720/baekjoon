import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

s,y,x = map(int,input().split())
y,x = y-1,x-1

queue = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            queue.append((i,j,board[i][j],0))
        board[i][j] = [board[i][j],0]



queue = deque(sorted(queue, key = lambda x: x[2]))

dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs():

    while queue:
        y,x,v,t = queue.popleft()
        if t > s-1:
            return
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny > n-1 or nx < 0 or nx > n-1 or board[ny][nx][0]:
                continue
            board[ny][nx] = [v,t+1]
            queue.append((ny,nx,v,t+1))

bfs()
print(board[y][x][0])