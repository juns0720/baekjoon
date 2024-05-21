import sys
from collections import deque
input = sys.stdin.readline

sy,sx = map(int,input().split())
ey,ex = map(int,input().split())
queue = deque([])
visited = [[0 for _ in range(9)] for _ in range(10)]

queue.append((sy,sx,0))
visited[sy][sx] = 1
def bfs(ey,ex):
    res = 0
    #상하좌우 먼저 이동
    dy = [0,-1,0,1]
    dx = [-1,0,1,0]
    #대각선 1칸씩 이동하면서 벽 있는지 검사
    pos = [[(-1,-1), (1,-1)], [(-1,-1), (-1,1)], [(-1,1), (1,1)], [(1,-1), (1,1)]]

    while queue:
        y,x,res = queue.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny == ey and nx == ex:
                continue
            if -1 < ny < 10 and -1 < nx < 9:
                for j in range(2):
                    ny2,nx2 = (ny,nx)
                    ty,tx = pos[i][j]
                    cnt = 0
                    for k in range(2):
                        ny2+=ty
                        nx2+=tx
                        if -1 < ny2 < 10 and -1 < nx2 < 9:
                            if k == 0 and ny2 == ey and nx2 == ex:
                                break
                            else:
                                cnt+=1
                    if cnt == 2 and not visited[ny2][nx2]:
                        if ny2 == ey and nx2 == ex:
                            return res+1                      
                        queue.append((ny2,nx2, res+1))
                        visited[ny2][nx2] = 1
    return -1

print(bfs(ey,ex))