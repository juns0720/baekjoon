import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

board = []
queue = deque([])
for y in range(N):
    temp = list(input().strip())
    for x in range(len(temp)):
        if temp[x] == 'I':
            queue.append((y,x))
    board.append(temp)

def BFS(y,x,cnt):
    while queue:
        (y,x) = queue.popleft()
        dy = [1,0,-1,0]
        dx = [0,1,0,-1]
        for i in range(4):
            ty = y+dy[i]
            tx = x+dx[i]
            if ty > -1 and ty < N and tx > -1 and tx < M and board[ty][tx] != 'X':
                    queue.append((ty,tx))
                    if board[ty][tx] == 'P':
                        cnt+=1
                    board[ty][tx] = 'X'
    return cnt
                
res = BFS(y,x,0)
if res == 0:
    print("TT")
else:
    print(res)

