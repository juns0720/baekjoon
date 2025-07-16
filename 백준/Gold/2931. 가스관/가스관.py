import sys
from collections import deque
input = sys.stdin.readline

pd = {
    '|' : [(-1,0),(1,0)],
    '-' : [(0,-1), (0,1)],
    '+' : [(0,-1),(0,1),(-1,0),(1,0)],
    '1' : [(1,0),(0,1)],
    '2' : [(-1,0),(0,1)],
    '3' : [(-1,0), (0,-1)],
    '4' : [(1,0),(0,-1)],
    'Z' : [],
    'M' : []

}
dy = [0,1,0,-1]
dx = [1,0,-1,0]


R,C = map(int,input().split())

board = []
start = [0,0]
e = [0,0]
for r in range(R):
    tmp = list(input().strip())
    for c in range(C):
        if tmp[c] == 'M':
            start[0] = r
            start[1] = c
        elif tmp[c] == 'Z':
            e[0] = r
            e[1] = c
    board.append(tmp)

queue = deque([])
visited = [[0 for _ in range(C)] for _ in range(R)]
visited[start[0]][start[1]] = 1

for d in range(4):
    ny = start[0] + dy[d]
    nx = start[1] + dx[d]
    if ny < 0 or ny > R-1 or nx < 0 or nx > C-1 or board[ny][nx] == '.':
        continue
    queue.append((ny,nx))
    visited[ny][nx] = 1

def bfs():
    while queue:
        y,x = queue.popleft()
        for dy,dx in pd[board[y][x]]:
            ny = y + dy
            nx = x + dx
            if ny < 0 or ny > R-1 or nx < 0 or nx > C-1 or visited[ny][nx]:
                continue
            if board[ny][nx] == '.':
                return (ny,nx)
            queue.append((ny,nx))
            visited[ny][nx] = 1

y,x = bfs()
ans = []
for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if ny < 0 or ny > R-1 or nx < 0 or nx > C-1 or board[ny][nx] == '.':
        continue
    for dy2,dx2 in pd[board[ny][nx]]:
        ny2 = ny + dy2
        nx2 = nx + dx2
        if ny2 < 0 or ny2 > R-1 or nx2 < 0 or nx2 > C-1:
            continue
        if (ny2,nx2) == (y,x):
            ans.append((ny-y,nx-x))
ans.sort()
for k,v in pd.items():
    if sorted(v) == ans:
        print(y+1,x+1,k)
        break