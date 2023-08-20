import sys
from collections import deque
input = sys.stdin.readline
N,L,R = map(int,input().split())

land = []
for i in range(N):
    land.append(list(map(int,input().split())))
def BFS(flag):
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    while queue:
        (y,x) = queue.popleft()
        visited[y][x] = 1
        tmp.append(land[y][x])
        tmp_pos.append((y,x))
        for i in range(4):
            ty = dy[i]+y
            tx = dx[i]+x
            if -1 < ty < N and -1 < tx < N and not visited[ty][tx]:
                val = abs(land[y][x] - land[ty][tx])
                if L-1 < val < R+1:
                    visited[ty][tx] = 1
                    queue.append((ty,tx))
    if len(tmp) > 1 or flag == True:
        flag = True
    return flag
day = 0
while True:
    line = [[0 for i in range(N)]for j in range(N)]
    queue = deque([])
    visited = [[0 for _ in range(N)]for _ in range(N)]
    flag = False
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                queue.append((y,x))
                tmp = []
                tmp_pos = deque([])
                flag = BFS(flag)
                avg = sum(tmp)//len(tmp)
                for ty,tx in tmp_pos:
                    land[ty][tx] = avg
    if flag == False:
        break
    else:
        day+=1
print(day)