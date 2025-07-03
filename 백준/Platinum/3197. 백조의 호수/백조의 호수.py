import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())

dy = [0,1,0,-1]
dx = [1,0,-1,0]

INF = sys.maxsize
board = [list(input().strip()) for _ in range(R)]
dist = [[INF for _ in range(C)] for _ in range(R)]

se = []
queue = deque()

for r in range(R):
    for c in range(C):
        if board[r][c] in ['.','L']:
            if board[r][c] == 'L':
                se.append((r,c))
            queue.append((r,c,0))
            dist[r][c] = 0
        

while queue:
    y,x,cost = queue.popleft()
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny > R-1 or nx < 0 or nx > C-1:
            continue
        if dist[ny][nx] <= cost+1:
            continue
        if board[ny][nx] == 'X':
            dist[ny][nx] = cost + 1
            queue.append((ny,nx,cost+1))


def bfs(day):
    queue2 = deque()
    while queue:
        y,x,crnt_day = queue.popleft()

        if (y,x) == (se[1][0],se[1][1]):
            return queue,day
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny > R-1 or nx < 0 or nx > C-1 or visited[ny][nx]:
                continue
            if dist[ny][nx] == day + 1:
                queue2.append((ny,nx,dist[ny][nx]))
                visited[ny][nx] = 1
            if dist[ny][nx] <= day:
                queue.append((ny,nx,dist[ny][nx]))
                visited[ny][nx] = 1
    return (queue2,-1)

day = 0
visited = [[0 for _ in range(C)] for _ in range(R)]
queue = deque([(se[0][0],se[0][1],0)])
visited[se[0][0]][se[0][1]] = 1

while day <= R*C:
    queue,res = bfs(day)
    if res > -1:
        print(res)
        break
    day+=1

