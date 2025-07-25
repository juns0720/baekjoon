import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

R,C = map(int,input().split())
k = int(input())
board = [[0 for _ in range(C)] for _ in range(R)]

for i in range(k):
    r,c = map(int,input().split())
    board[r][c] = -1
sy,sx = map(int,input().split())

dir = list(map(int,input().split()))

for i in range(len(dir)):
    dir[i]-=1
queue = deque([(sy,sx,0)])
board[sy][sx] = 1
def bfs():

    while queue:
        y,x,di = queue.popleft()
        flag = 1
        for i in range(4):
            curr_d = dir[(di+i)%4]
            ny = y + dy[curr_d]
            nx = x + dx[curr_d]
            if ny < 0 or ny > R-1 or nx < 0 or nx > C-1 or board[ny][nx] in [1,-1]:
                continue
            queue.append((ny,nx,di+i))
            board[ny][nx] = 1
            flag = 0
            break
        if flag:
            print(y,x)
            return
bfs()