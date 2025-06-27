from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1, -2),(-1, 2),(-2, -1),(-2, 1),(1, -2),(1, 2),(2, -1),(2, 1)]
INF = 10 ** 4

n,m = map(int, input().split())
vi = [[INF] * n for _ in range(n)]
q = deque()

a, b = map(int, input().split())
q.append((a-1, b-1))
vi[q[0][0]][q[0][1]] = 0

taget = []
for _ in range(m):
    a, b = map(int, input().split())
    taget.append((a-1, b-1))



while q:
    cr, cc = q.popleft()
    
    for dr, dc in dir:
        nr = cr + dr
        nc = cc + dc 

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue

        if vi[nr][nc] > vi[cr][cc] and vi[nr][nc] == INF:
            vi[nr][nc] = vi[cr][cc] + 1
            q.append((nr,nc))


for i, j in taget:
    print(vi[i][j], end=' ')