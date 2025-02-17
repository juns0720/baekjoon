import sys
input = sys.stdin.readline

r,c,q = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(r)]

prefix = [[0 for _ in range(c+1)] for _ in range(r+1)]


for i in range(1,r+1):
    for j in range(1,c+1):
        prefix[i][j] = board[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

for i in range(q):
    sy,sx,ey,ex = map(int,input().split())
    total = (ey-sy+1) * (ex-sx+1)
    res = prefix[ey][ex] - prefix[sy-1][ex] - prefix[ey][sx-1] + prefix[sy-1][sx-1]

    print(res//total)