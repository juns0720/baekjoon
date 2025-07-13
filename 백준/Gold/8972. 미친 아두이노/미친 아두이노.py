import sys
from collections import deque
input = sys.stdin.readline

dy = [1,1,1,0,0,0,-1,-1,-1]
dx = [-1,0,1,-1,0,1,-1,0,1]

R,C = map(int,input().split())
board = [['.' for _ in range(C)] for _ in range(R)]
queue = deque([])
for r in range(R):
    col = list(input().strip())
    for c in range(C):
        if col[c] == 'I':
            sy,sx = r,c
        elif col[c] == 'R':
            queue.append((r, c, 'R', 0))
queue.append((sy, sx, 'I', 0))
queue.rotate(1)
md = list(map(int,input().strip()))
n = len(md)

def find():
    robot_q = deque([])
    robot = dict()
    while queue:
        y,x,w,cnt = queue.popleft()
        if w == 'I':
            if cnt > n-1:
                board[y][x] = w
                return robot_q, robot
            sy = y + dy[md[cnt]-1]
            sx = x + dx[md[cnt]-1]
            while robot_q:
                ry,rx,w2,cnt2 = robot_q.popleft()
                if robot[(ry,rx)] > 1:
                    continue
                queue.append((ry,rx,w2,cnt2))
            
            queue.append((sy,sx,w,cnt+1))
            robot = dict()
        else:
            min_dist = R*C+1
            ey,ex = y,x
            for i in range(9):
                ny = y + dy[i]
                nx = x + dx[i]
                cur_dist = abs(sy-ny) + abs(sx-nx)
                if cur_dist < min_dist:
                    ey,ex = ny,nx
                    min_dist = cur_dist
            if (ey,ex) in robot:
                robot[(ey,ex)] += 1
                continue
            robot[(ey,ex)] = 1
            robot_q.append((ey,ex,w,cnt+1))
            if (ey,ex) == (sy,sx):
                print("kraj",cnt+1)
                exit()
robot_q, robot = find()

while robot_q:
    y,x,w,cnt = robot_q.popleft()
    if robot[(y,x)] > 1:
        continue
    board[y][x] = w
for r in range(R):
    for c in range(C):
        print(board[r][c], end='')
    print()