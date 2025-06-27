import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())

dy = [0,-1,0,1]
dx = [-1,0,1,0]

board = [list(input().strip()) for _ in range(R)]

def bfs2(sy,sx):
    queue = deque([(sy,sx)])
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny > R-1 or nx < 0 or nx > C-1 or board[ny][nx] =='.':
                continue
            if ny == R-1:
                up.clear()
                return 0
            if not visited[ny][nx]:
                up.append((ny,nx))
                queue.append((ny,nx))
                visited[ny][nx] = 1
    return 1

def move():
    min_height = R+1
    up.sort(key = lambda x: -x[0])
    for y,x in up:
        cnt = 0
        for ny in range(y+1,R):
            if visited[ny][x] == 1:
                cnt = R+1
                break
            if board[ny][x] == '.':
                cnt += 1
            else:
                break
        min_height = min(min_height,cnt)
    
    for y,x in up:
        board[y][x] = '.'
        board[y+min_height][x] = 'x'


def print_result():
    for i in board:
        print(''.join(i))


# d가 짝수면 왼쪽, 홀수면 오른쪽
int(input())
d = 0
heights = list(map(int,input().split()))
for h in heights:
    exist = 0
    up = []
    h = R-h
    if d % 2 == 0:
        for x in range(C):
            if board[h][x] == 'x':
                board[h][x] = '.'
                visited = [[0 for _ in range(C)] for _ in range(R)]
                break
    else:
        for x in range(C-1,-1,-1):
            if board[h][x] == 'x':
                board[h][x] = '.'
                visited = [[0 for _ in range(C)] for _ in range(R)]
                break           
    for j in range(4):
        nh = h + dy[j]
        nx = x + dx[j]
        if nh < 0 or nh > R-1 or nx < 0 or nx > C-1:
            continue
        if board[nh][nx] == 'x': 
            up.append((nh,nx))
            visited[nh][nx] = 1
            exist = bfs2(nh,nx)
        if exist:
            break
        visited = [[0 for _ in range(C)] for _ in range(R)]

    #아래로 내리기
    if up:
        move()
    d+=1
print_result()

            