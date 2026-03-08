import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0]*(M+2) for _ in range(N+2)]
vis = [[0]*(M+2) for _ in range(N+2)]

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]

for i in range(1, N+1):
    row = list(map(int, input().split()))
    for j in range(1, M+1):
        arr[i][j] = row[j-1]

for i in range(2, M+2):
    arr[0][i] = 1
for i in range(0, M):
    arr[N+1][i] = 1
for i in range(2, N+1):
    arr[i][0] = 1
for i in range(1, N):
    arr[i][M+1] = 1

dq = deque()
dq.append((0, M+1, 1))
vis[0][M+1] = 1

while dq:
    cy, cx, cc = dq.popleft()
    if cy == N+1 and cx == 0:
        break

    for i in range(8):
        ny = cy + dy[i]
        nx = cx + dx[i]

        if ny < 0 or nx < 0 or ny > N+1 or nx > M+1:
            continue
        if ny == 1 and nx == 1:
            continue
        if ny == N and nx == M:
            continue

        nc = cc + (1 if arr[ny][nx] == 0 else 0)

        if vis[ny][nx] > 0 and vis[ny][nx] <= nc:
            continue

        vis[ny][nx] = nc

        if arr[ny][nx] == 1:  # 벽
            dq.appendleft((ny, nx, nc))
        else:  # 빈공간
            dq.append((ny, nx, nc))

print(vis[N+1][0] - 1)