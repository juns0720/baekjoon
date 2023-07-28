import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
board = [list(input().strip()) for _ in range(N)]
queue = deque([])
cnt = 0
point = []
def BFS(y,x):
    queue.append((y,x))
    cnt = 1
    board[y][x] = 0
    while queue:
        (y,x) = queue.popleft()

        dy = [0,-1,0,1]
        dx = [-1,0,1,0]
        for i in range(4):
            (ty,tx) =(y+dy[i],x+dx[i])
            if ty > -1 and ty < N and tx > -1 and tx < N:
                if board[ty][tx] == '1':
                    queue.append((ty,tx))   
                    board[ty][tx] = 0
                    cnt+=1
    return cnt

for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            point.append(BFS(i,j))
            cnt+=1
print(cnt)
for index in sorted(point):
    print(index)
