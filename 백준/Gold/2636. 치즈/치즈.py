import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]
queue = deque([])

def BFS():
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    cnt = 0
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ty = y+dy[i]
            tx = x+dx[i]
            if -1 < ty < N and -1 < tx < M and not visited[ty][tx]:
                if board[ty][tx] == 0 :
                    queue.append((ty,tx))
                    visited[ty][tx] = 1
                    board[ty][tx] = 0
                elif board[ty][tx] == 1:
                    board[ty][tx] = 0
                    visited[ty][tx] = 1
                    cnt+=1
    if cnt == 0:
        return -1
    else:
        return cnt

cnt1 = 0
cnt2 = 1
res = []
while True:
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 0
    queue.append((0,0))
    cnt2 = BFS()
    res.append(cnt2)
    if cnt2 == -1:
        break
    cnt1+=1
print(cnt1)
print(res[-2])