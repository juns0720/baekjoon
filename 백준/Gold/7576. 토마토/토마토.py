import sys
input = sys.stdin.readline
from collections import deque

X,Y = map(int,input().split())

visited = [[0 for _ in range(X)] for _ in range(Y)]
box = [list(map(int,input().split())) for _ in range(Y)]
queue = deque([])
max_res = 0
min_res = False
# x,y = 시작 좌표
# tx,ty = 현재 좌표

def BFS(x,y,X,Y):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    for y1 in range(Y):
        for x1 in range(X):
            if box[y1][x1] == 1:
                queue.append((y1,x1))
    while queue:
        (ay,ax) = queue.popleft()
        for i in range(4):
            ny = ay+dy[i]
            nx = ax+dx[i]
            if ny < Y and ny > -1 and nx < X and nx > -1:
                if box[ny][nx] != -1:
                    if box[ny][nx] < 1:
                        box[ny][nx] = max(box[ay][ax]+1,box[ny][nx])
                        queue.append((ny,nx))



BFS(0,0,X,Y)
for i in box:
    max_res = max(max(i),max_res)
    if 0 in i:
        min_res = True

if min_res == True:
    print(-1)
else:
    print(max_res-1)