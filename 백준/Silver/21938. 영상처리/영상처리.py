import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
tmp = []
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    tmp.append(list(map(int,input().split())))
 
T = int(input())

display = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        avg = (tmp[i][3*j]+tmp[i][3*j+1]+tmp[i][3*j+2])//3
        display[i][j] = 255 if avg >= T else avg



cnt = 0
def bfs():
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            
            if -1 < ny < N and -1 < nx < M and not visited[ny][nx]:
                if display[ny][nx] == 255:
                    queue.append((ny,nx))
                    visited[ny][nx] = 1
    return 1


for row in range(N):
    for col in range(M):
        if display[row][col] == 255 and not visited[row][col]:
            queue = deque([])
            queue.append((row,col))
            visited[row][col]
            cnt+=bfs()
print(cnt)
