import sys
from collections import deque
input = sys.stdin.readline
d = [(0,1), (1,0), (-1,0), (0,-1)]

n = int(input())

board = []
for r in range(n):
    tmp = list(input().strip())
    for c in range(n):
        if tmp[c] == '#':
            sy,sx = r,c
            break
    board.append(tmp)

def search(sy,sx):
    queue = deque([(sy,sx, 0)])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[sy][sx] = 1
    while queue:
        y,x,cost = queue.popleft()

        for i in range(4):
            for j in range(1,n):
                ny = y + d[i][0] * j
                nx = x + d[i][1] * j

                if ny < 0 or ny > n-1 or nx < 0 or nx > n-1 or board[ny][nx] == '*':
                    break
                if visited[ny][nx]:
                    continue

                if board[ny][nx] == '!':
                    queue.append((ny,nx,cost+1))
                    visited[ny][nx] = 1
                elif board[ny][nx] == '#':
                    return cost
                
    return cost
res = search(sy,sx)
print(res)