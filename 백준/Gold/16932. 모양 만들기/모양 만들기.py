import sys
from collections import deque
input = sys.stdin.readline

dy = [0,1,0,-1]
dx = [1,0,-1,0]

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]



def bfs(y,x,key):
    queue = deque([(y,x)])
    cnt = 1
    while queue:
        y,x= queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny > n-1 or nx < 0 or nx > m-1 or visited[ny][nx]:
                continue
            if board[ny][nx] == 1:
                board[ny][nx] = key
                queue.append((ny,nx))
                visited[ny][nx] = 1
                cnt+=1

    return cnt

res = 0
area = {}
key = 2

visited = [[0 for _ in range(m)] for _ in range(n)]
for r in range(n):
    for c in range(m):
        if board[r][c] == 1 and not visited[r][c]:
            board[r][c] = key
            area[key] = bfs(r,c,key)
            key+=1

res = 0
for y in range(n):
    for x in range(m):
        cnt = 1
        cache = set()
        if board[y][x] != 0:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny > n-1 or nx < 0 or nx > m-1 or board[ny][nx] == 0:
                continue
            cache.add(board[ny][nx])
        for i in cache:
            cnt += area[i]
        res = max(res,cnt)
print(res)