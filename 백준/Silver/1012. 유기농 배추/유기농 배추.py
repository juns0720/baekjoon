import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS():

    while queue:
        y,x = queue.popleft()
        board[y][x] = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx > -1 and nx < M and ny > -1 and ny < N and board[ny][nx] != 0:
                if board[ny][nx] == 1:
                    board[ny][nx] = 0
                    queue.append((ny,nx))

T = int(input())
for i in range(T):
    queue = deque([])
    M,N,K = map(int,input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x,y = map(int,input().split())
        board[y][x] = 1

    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                queue.append((y,x))
                BFS()
                cnt +=1
    print(cnt)