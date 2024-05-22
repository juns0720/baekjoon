import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
flag = True
cnt = 0
total_cheese = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            total_cheese+=1

def Bfs():
    queue = deque([])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue.append((0,0))
    visited[0][0] = 1
    global cnt
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    contact_cnt = 0
    while queue:

        y,x = queue.popleft()
        for i in range(4):
            ty = y+dy[i]
            tx = x+dx[i]
            if -1 < ty < N and -1 < tx < M and not visited[ty][tx]:
                if board[ty][tx] == 1:
                    contact_cnt = 0
                    for j in range(4):
                        ey = ty+dy[j]
                        ex = tx+dx[j]
                        if -1 < ey < N and -1 < ex < M and not visited[ty][tx]:
                            if board[ey][ex] == 2:
                                contact_cnt += 1
                    if contact_cnt > 1:
                        board[ty][tx] = -1
                        visited[ty][tx] = 1
                else:
                    queue.append((ty,tx))
                    visited[ty][tx] = 1
    cnt+=1
    return

def bfs_air():
    queue = deque([])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue.append((0,0))
    visited[0][0] = 1
    cheese = 0
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    flag = False
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ty = y+dy[i]
            tx = x+dx[i]
            if -1 < ty < N and -1 < tx < M and not visited[ty][tx]:
                if board[ty][tx] == 2 or board[ty][tx] == -1 or board[ty][tx] == 0:
                    if board[ty][tx] == -1:
                        flag = True
                        cheese+=1
                    board[ty][tx] = 2
                    visited[ty][tx] = 1
                    queue.append((ty,tx))
    return cheese
                    

while True:
    total_cheese -= bfs_air()
    if total_cheese == 0:
        break
    Bfs()

        
print(cnt)
