import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
visited = [[INF for _ in range(m)] for _ in range(n)]
queue = deque([])

for y in range(n):
    for x in range(m):
        if board[y][x]:
            queue.append((y,x))
            visited[y][x] = 0

dy = [0,1,0,-1,1,1,-1,-1]
dx = [1,0,-1,0,1,-1,1,-1]

def bfs():
    max_dist = 0
    while queue:
        y,x = queue.popleft()
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny > n-1 or nx < 0 or nx > m-1:
                continue
            if  visited[y][x] + 1 < visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny,nx))
                max_dist = max(max_dist,visited[ny][nx])
    return max_dist

print(bfs())