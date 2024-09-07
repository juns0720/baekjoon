import sys
from collections import deque
input = sys.stdin.readline

'''
1. 물이 이동 가능한 장소 : 아무것도 없는 칸
2. 고슴도치가 이동할 수 있는 장소 : D 혹은 .
'''

dy = [0,1,0,-1]
dx = [1,0,-1,0]

R,C = map(int,input().split())
board = []
queue = deque()
visited = [[0 for _ in range(C)] for _ in range(R)]
for row in range(R):
    tmp = list(input().strip())
    for col in range(len(tmp)):
        if tmp[col] == 'S':
            queue.append((row,col,0))
            visited[row][col] = 1
    board.append(tmp)

def diffusion():
    water = []
    for row in range(R):
        for col in range(C):
            if board[row][col] == '*':
                water.append((row,col))
    for y,x in water:
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if -1 < ny < R and -1 < nx < C and board[ny][nx] == '.':
                board[ny][nx] = '*'
def BFS():
    prev_dist = -1
    while queue:
        y,x,dist = queue.popleft()
        if prev_dist < dist:
            diffusion()
        prev_dist = dist

        if board[y][x] == 'D':
            print(dist)
            exit()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if -1 < ny < R and -1 < nx < C:
                if visited[ny][nx]:
                    continue
                if board[ny][nx] == '.' or board[ny][nx] == 'D':
                    queue.append((ny,nx,dist+1))
                    visited[ny][nx] = 1
        

BFS()
print("KAKTUS")