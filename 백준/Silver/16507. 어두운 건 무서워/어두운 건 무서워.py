import sys
input = sys.stdin.readline

r,c,q = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(r)]

prefix = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
    prefix[i][0] = board[i][0]

for i in range(r):
    for j in range(1,c):
        prefix[i][j] = prefix[i][j-1]+board[i][j]

for i in range(q):
    sy,sx,ey,ex = map(int,input().split())
    sy,ey = min(sy-1,ey-1), max(sy-1,ey-1)
    sx,ex = min(sx-1,ex-1), max(sx-1,ex-1)

    res = 0
    for j in range(sy,ey+1):
        res+= prefix[j][ex] if sx == 0 else (prefix[j][ex]-prefix[j][sx-1])
    total = (ey-sy+1) * (ex-sx+1)
    print(res//total)