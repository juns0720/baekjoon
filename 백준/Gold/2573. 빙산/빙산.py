import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs():
    n_pos = []
    while queue:
        y,x = queue.popleft()
        nc = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or ny > N-1 or nx < 0 or nx > M-1:
                continue
            if board[ny][nx] == 0:
                nc += 1
        n_pos.append((y,x,nc))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny > N-1 or nx < 0 or nx > M-1 or visited[ny][nx] or board[ny][nx] < 1:
                continue

            queue.append((ny,nx))
            visited[ny][nx] = 1
    return n_pos

            
def melt():
    n_pos = []
    for y,x,c in pos:
        if board[y][x] > 0:
            nc = board[y][x] - c
            if nc < 0:
                nc = 0
            board[y][x] = nc
            if nc > 0:
                n_pos.append((y,x,0))
    return n_pos
pos = []
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            pos.append((i,j,0))

if len(pos) == 0:
    print(0)
    exit()

for i in range(300):
    queue = deque([])
    visited = [[0 for _ in range(M)] for _ in range(N)]

    y,x,c = pos[0]
    queue.append((y,x))
    visited[y][x] = 1

    target = len(pos)
    pos = bfs()
    if len(pos) != target:
        print(i)
        exit()

    pos = melt()
    if len(pos) == 0:
        print(0)
        exit()
print(0)