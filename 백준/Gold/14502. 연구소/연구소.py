import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N,M = map(int,input().split())
pos = []
board = []
queue = deque([])
virus = []
Max = 0
for i in range(N):
    temp = list(map(int,input().split()))
    board.append(temp)
    for j in range(len(temp)):
        if temp[j] == 0:
            pos.append((i,j))
        elif temp[j] == 2:
            virus.append((i,j))
def BFS():
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ty = y+dy[i]
            tx = x+dx[i] 
            if ty < N and ty > -1 and tx < M and tx > -1:
                if board2[ty][tx] == 0:
                    board2[ty][tx] = 2
                    queue.append((ty,tx))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board2[i][j] == 0:
                cnt+=1
    return cnt

for wall in combinations(pos,3):
    board2 = deepcopy(board)
    for i in virus:
        queue.append(i)
    for i in wall:
        board2[i[0]][i[1]] = 1
    Max = max(BFS(),Max)
print(Max)