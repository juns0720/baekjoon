import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
x,y = 0,0
start = False
dmap = []
queue = deque([])
visited = [[-1 for i in range(N)]for _ in range(M)]
for ny in range(N):
    line = list(map(int,input().split()))
    dmap.append(line)
    for nx in range(len(line)):
        if line[nx] == 2:
            y = ny
            x = nx
            start = True
        elif line[nx] == 1:
            line[nx] = -1

def BFS(y,x):
    queue.append((y,x))
    dmap[y][x] = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while queue:
        (ny,nx) = queue.popleft()
        for i in range(4):
            ty = dy[i]+ny
            tx = dx[i]+nx
            if ty > -1 and ty < N and tx > -1 and tx < M and dmap[ty][tx] == -1:
                if dmap[ty][tx] != 0:
                    queue.append((ty,tx))
                    dmap[ty][tx] = dmap[ny][nx]+1
                
BFS(y,x)
for i in dmap:
    s = ''
    for j in i:
        s+=(str(j)+' ')
    print(s)