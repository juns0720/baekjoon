import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
N,m = map(int,input().split())
virus = []
board = []
cnt = 0
for r in range(N):
    col = list(map(int,input().split()))
    for c in range(N):
        if col[c] == 2:
            virus.append((r,c))
            cnt += 1
        if col[c] == 0:
            cnt += 1
    board.append(col)


dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs():

    cost = 0
    check = m
    while queue:
        y,x,c = queue.popleft()
        cost = max(c, cost)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny > N-1 or nx < 0 or nx > N-1 or visited[ny][nx] or board[ny][nx] == 1:
                continue
            queue.append((ny,nx,c+1))
            visited[ny][nx] = 1
            check += 1
    if cnt != check:
        return INF
    return cost

min_cost = INF
for curr_virus in combinations(virus,m):
    queue = deque([])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for y,x in curr_virus:
        queue.append((y,x,0))
        visited[y][x] = 1
    min_cost = min(bfs(), min_cost)

if min_cost == INF:
    min_cost = -1
print(min_cost)
