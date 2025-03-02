import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]


def move(y, x, dy, dx):
    cnt = 0
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        cnt += 1
    return (y,x,cnt)


def bfs():
    while queue:
        ry, rx, by, bx, cnt = queue.popleft()
        if cnt > 10:
            return -1
        for i in range(4):
            nry,nrx,rcnt = move(ry,rx,dy[i],dx[i])
            nby,nbx,bcnt = move(by,bx,dy[i],dx[i])
            if board[nby][nbx] == 'O':
                continue
            if board[nry][nrx] == 'O':
                return cnt
            if nry == nby and nrx == nbx:
                if rcnt > bcnt:
                    nry -= dy[i]
                    nrx -= dx[i]
                else:
                    nby -= dy[i]
                    nbx -= dx[i]
            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = 1
                queue.append((nry,nrx,nby,nbx,cnt+1))
    return -1
visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
for r in range(n):
    for c in range(m):
        if board[r][c] == 'R':
            ry,rx = r,c
        elif board[r][c] == 'B':
            by,bx = r,c
queue = deque([(ry,rx,by,bx,1)])
visited[ry][rx][by][bx] = 1
print(bfs())