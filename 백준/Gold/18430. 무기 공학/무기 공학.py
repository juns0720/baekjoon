import sys
input = sys.stdin.readline

dy = [0,1,0,-1]
dx = [1,0,-1,0]
n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

if n*m <= 4:
    print(0)
    exit()


def check(s,w):
    global res
    res = max(res,w)
    for i in range(s,n*m):
            y,x = i//m,i%m
            if visited[y][x]:
                continue    
            visited[y][x] = 1
            for j in range(4):
                    ny1,nx1 = y + dy[j], x + dx[j]
                    ny2,nx2 = y + dy[(j+1)%4], x + dx[(j+1)%4]
                    if ny1 < 0 or ny1 > n-1 or nx1 < 0 or nx1 > m-1 or visited[ny1][nx1]:
                        continue
                    if ny2 < 0 or ny2 > n-1 or nx2 < 0 or nx2 > m-1 or visited[ny2][nx2]:
                        continue
                    visited[ny1][nx1] = 1
                    visited[ny2][nx2] = 1
                    check(i+1,w+board[y][x]*2+board[ny1][nx1]+board[ny2][nx2])
                    visited[ny1][nx1] = 0
                    visited[ny2][nx2] = 0
            visited[y][x] = 0

res = 0
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n*m):
    y,x = i//m,i%m
    visited[y][x] = 1
    for j in range(4):
            ny1,nx1 = y + dy[j], x + dx[j]
            ny2,nx2 = y + dy[(j+1)%4], x + dx[(j+1)%4]
            if ny1 < 0 or ny1 > n-1 or nx1 < 0 or nx1 > m-1:
                continue
            if ny2 < 0 or ny2 > n-1 or nx2 < 0 or nx2 > m-1:
                continue
            visited[ny1][nx1] = 1
            visited[ny2][nx2] = 1
            check(i+1,board[y][x]*2+board[ny1][nx1]+board[ny2][nx2])
            visited[ny1][nx1] = 0
            visited[ny2][nx2] = 0
    visited[y][x] = 0
print(res)