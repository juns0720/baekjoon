import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]
queue = deque([])
def BFS1(color):
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ty = dy[i]+y
            tx = dx[i]+x
            if -1 < tx < N and -1 < ty < N and not visited1[ty][tx]:
                if (color == 'R' and board[ty][tx] == 'G') or (color == 'G' and board[ty][tx] == 'R'):
                    visited1[ty][tx] = 1
                    queue.append((ty,tx))
                elif board[ty][tx] == color:
                    visited1[ty][tx] = 1
                    queue.append((ty,tx))
def BFS2(color):
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ty = dy[i]+y
            tx = dx[i]+x
            if -1 < tx < N and -1 < ty < N and not visited2[ty][tx] and board[ty][tx] == color:
                    visited2[ty][tx] = 1
                    queue.append((ty,tx))
visited1 = [[0 for _ in range(N)] for _ in range(N)]
visited2 = [[0 for _ in range(N)] for _ in range(N)]
cnt = [0,0]
for y in range(N):
    for x in range(N):
        if visited1[y][x] == 0:
            queue.append((y,x))
            visited1[y][x] = 1
            BFS1(board[y][x])
            cnt[1]+=1
        if visited2[y][x] == 0:
            queue.append((y,x))
            visited2[y][x] = 1
            BFS2(board[y][x])
            cnt[0]+=1

print(cnt[0],cnt[1])