import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

board = [list(input().strip()) for _ in range(N)]

if N < 3:
    print(0)
    exit()
visited = [[0 for _ in range(N)] for _ in range(N)]
for r,c,nr,nc in [(0,0, 1,1),(0,N-1, 1,N-2),(N-1,0, N-2,1),(N-1,N-1, N-2,N-2)]:
    if visited[r][c]:
        continue
    visited[r][c] = 1

    if visited[nr][nc]:
        continue


    if board[r][c] == '0':
        board[nr][nc] = 'x'
    else:
        board[nr][nc] = 'o'

    visited[nr][nc] = 1

visited[0][1], visited[0][-2] = 1,1
visited[1][0], visited[1][-1] = 1,1
visited[-1][1], visited[-1][-2] = 1,1
visited[-2][0], visited[-2][-1] = 1,1



#가로
queue = deque([(0,1,1,1),(0,N-2,-1,1),(N-1,1,1,-1),(N-1,N-2,-1,-1)])
while queue:
    y,x,dx,dy = queue.popleft()

    ny = y+dy
    nx = x+dx

    if visited[y][nx]:
        continue

    visited[y][nx] = 1
    queue.append((y,nx,dx,dy))

    if visited[ny][nx]:
        continue

    visited[ny][nx] = 1

    if board[y][x] == '3':
        board[ny][nx] = 'o'

    elif board[y][x] == '2':
        if board[ny][x-1:x+2].count('o') == 1:
            board[ny][nx] = 'o'
        else:
            board[ny][nx] = 'x'

    elif board[y][x] == '1':
        if board[ny][x-1:x+2].count('o') == 0:
            board[ny][nx] = 'o'
        else:
            board[ny][nx] = 'x'            

    else:
        board[ny][nx] = 'x'



#세로
queue = deque([(1,0,1,1),(N-2,0,1,-1),(1,N-1,-1,1),(N-2,N-1,-1,-1)])
while queue:
    y,x,dx,dy = queue.popleft()

    ny = y + dy
    nx = x + dx

    if visited[ny][x]:
        continue
    visited[ny][x] = 1
    queue.append((ny,x,dx,dy))

    if visited[ny][nx]:
        continue
    visited[ny][nx] = 1

    if board[y][x] == '3':
        board[ny][nx] = 'o'

    elif board[y][x] == '2':
        if [board[y-1][nx],board[y][nx],board[y+1][nx]].count('o') == 1:
            board[ny][nx] = 'o'
        else:
            board[ny][nx] = 'x'

    elif board[y][x] == '1':
        if [board[y-1][nx],board[y][nx],board[y+1][nx]].count('o') == 0:
            board[ny][nx] = 'o'
        else:
            board[ny][nx] = 'x'            

    else:
        board[ny][nx] = 'x'


res = 0

for c in range(1,N-1):
    res += board[c].count('o')

least = 0
if N > 3:
    least = (N-4)**2

print(res + least)