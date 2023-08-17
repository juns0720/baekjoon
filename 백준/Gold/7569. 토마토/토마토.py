import sys
input = sys.stdin.readline
from collections import deque

X,Y,Z= map(int,input().split())

visited = [[[0 for _ in range(X)] for _ in range(Y)] for _ in range(Z)]
box = [[list(map(int,input().split())) for _ in range(Y)] for _ in range(Z)]
queue = deque([])
max_res = 0
grow = True
# x,y = 시작 좌표
# tx,ty = 현재 좌표

def BFS(x,y,z):
    dz = [1,-1,0,0,0,0]
    dy = [0,0,0,1,0,-1]
    dx = [0,0,1,0,-1,0]
    for z1 in range(Z):
        for y1 in range(Y):
            for x1 in range(X):
                if box[z1][y1][x1] == 1:
                    queue.append((z1,y1,x1))
    while queue:
        (az,ay,ax) = queue.popleft()
        for i in range(6):
            nz = az+dz[i]
            ny = ay+dy[i]
            nx = ax+dx[i]
            if nz < Z and nz > -1 and ny < Y and ny > -1 and nx < X and nx > -1 :
                if box[nz][ny][nx] != -1:
                    if box[nz][ny][nx] < 1:
                        box[nz][ny][nx] = box[az][ay][ax]+1
                        queue.append((nz,ny,nx))

BFS(0,0,0)
for i in box:
    for j in i:
        max_res = max(max(j),max_res)
        if 0 in j:
            grow = False
            break

if grow == False:
    print(-1)
elif max_res == 1:
    print(0)
else:
    print(max_res-1)