import sys
from collections import deque
input = sys.stdin.readline
R,C = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(R)]
dy = [0,0,1,-1]
dx = [1,-1,0,0]
sy,sx,sd = map(int,input().split())
ey,ex,ed = map(int,input().split())
sy,sx,sd = sy-1,sx-1,sd-1
ey,ex,ed = ey-1,ex-1,ed-1

INF = sys.maxsize
dist = [[[INF,INF,INF,INF] for _ in range(C)] for _ in range(R)]
queue = deque([(sy,sx,sd)])
dist[sy][sx][sd] = 0
def bfs():
    while queue:
        y,x,d = queue.popleft()

        for i in range(4):
            if d == i:
                continue
            if d+i in [1,5]:
                if dist[y][x][i] > dist[y][x][d] + 2:
                    dist[y][x][i] = dist[y][x][d] + 2
                    queue.append((y,x,i))
            else:
                if dist[y][x][i] > dist[y][x][d] + 1:
                    dist[y][x][i] = dist[y][x][d] + 1
                    queue.append((y,x,i))

            
        for j in range(1,4):
            ny = y + dy[d]*j
            nx = x + dx[d]*j
            if ny < 0 or ny > R-1 or nx < 0 or nx > C-1 or board[ny][nx] == 1:
                break
            if dist[ny][nx][d] > dist[y][x][d] + 1:
                dist[ny][nx][d] = dist[y][x][d]+1
                queue.append((ny,nx,d))

bfs()
print(dist[ey][ex][ed])