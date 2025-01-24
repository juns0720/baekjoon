import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]


dy = [0,1,0,-1]
dx = [1,0,-1,0]
max_dist = 0
res = 0

def bfs(s):
    global max_dist,res
    while queue:
        y,x,dist = queue.popleft()
        if (y == 0 or y == n-1 or x == 0 or x == m-1):
            if max_dist == dist:
                res = max(res,s + board[y][x])
            elif max_dist < dist:
                res = s + board[y][x]
                max_dist = dist

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if nx < 0 or nx > m-1 or ny < 0 or ny > n-1 or visited[ny][nx] or board[ny][nx] == 0:
                continue
            visited[ny][nx] = 1
            queue.append([ny,nx,dist+1])

for r in range(n):
    for c in range(m):
        if board[r][c] == 0:
            continue
        queue = deque()
        queue.append((r,c,0))
        visited = [[0 for _ in range(m)] for _ in range(n)]
        visited[r][c] = 1
        bfs(board[r][c])

print(res)