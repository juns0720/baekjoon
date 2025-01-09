import sys
input = sys.stdin.readline
R,C,K = map(int,input().split())

board = [list(input().strip()) for _ in range(R)]
sy,sx = R-1,0
res = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def dfs(y,x,dist):
    global res
    if (y,x) == (0,C-1) and dist == K:
        res+=1
    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        if ny < 0 or ny > R-1 or nx < 0 or nx > C-1 or visited[ny][nx] or board[ny][nx] == 'T':
            continue
        visited[ny][nx] = 1
        dfs(ny,nx,dist+1)
        visited[ny][nx] = 0
visited = [[0 for _ in range(C)] for _ in range(R)]
visited[sy][sx] = 1
dfs(sy,sx,1)
print(res)