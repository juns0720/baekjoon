import sys
from collections import deque
input = sys.stdin.readline

dy = [-2,-2,-1,-1,1,1,2,2]
dx = [-1,1,-2,2,-2,2,-1,1]


n,m = map(int,input().split())

board = [[0 for _ in range(n)] for _ in range(n)]

y,x = map(int,input().split())
y,x = y-1,x-1
def bfs():
    while queue:
        y,x,cnt = queue.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny > n-1 or nx < 0 or nx > n-1 or visited[ny][nx]:
                continue
            queue.append((ny,nx,cnt+1))
            visited[ny][nx] = 1
            board[ny][nx] = cnt+1

visited = [[0 for _ in range(n)] for _ in range(n)]
visited[y][x] = 1
queue = deque([(y,x,0)])
bfs()
for _ in range(m):
    hy,hx = map(int,input().split())
    hy,hx = hy-1,hx-1
    print(board[hy][hx], end = ' ')