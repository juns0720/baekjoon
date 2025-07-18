import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
dy = [0,1,0,-1]
dx = [1,0,-1,0]

N,M = map(int,input().split())
sy,sx = map(int,input().split())
ey,ex = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]




dic = dict()
def bfs(sy,sx,flag):
    global res
    queue = deque([(sy,sx,0)])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[sy][sx] = 1
    while queue:
        y,x,dist = queue.popleft()
        if flag and (y,x) == (ey-1,ex-1):
            res = min(res, dist)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny > N-1 or nx < 0 or nx > M-1 or visited[ny][nx]:
                continue
            if board[ny][nx] == 1:
                if (ny,nx) in dic:
                    dic[(ny,nx)][1] += dist+1
                    dic[(ny,nx)][0] += 1
                else:
                    dic[(ny,nx)] = [1,dist+1]
                visited[ny][nx] = 1
                continue
            queue.append((ny,nx,dist+1))
            visited[ny][nx] = 1
    
res = sys.maxsize 
bfs(sy-1,sx-1,1)
bfs(ey-1,ex-1,0)

lst = sorted(list(dic.values()),key = lambda x : (-x[0],x[1]))
if lst[0][0] != 2:
    print(-1)
    exit()
res = min(res,lst[0][1])
if res == sys.maxsize:
    res = -1
print(res)