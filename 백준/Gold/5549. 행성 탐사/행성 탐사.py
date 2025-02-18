import sys
input = sys.stdin.readline

m,n = map(int,input().split())
q = int(input())
board = [list(input().strip()) for _ in range(m)]
prefix = [[[0,0,0] for _ in range(n+1)] for _ in range(m+1)]
# J = 0, O = 1, I = 2
for i in range(1,m+1):
    for j in range(1,n+1):
        if board[i-1][j-1] == 'J':
            least = 0
        elif board[i-1][j-1] == "O":
            least = 1
        else:
            least = 2
        for k in range(3):
            if least == k:
                prefix[i][j][k] = 1 + prefix[i-1][j][k] + prefix[i][j-1][k] - prefix[i-1][j-1][k]
            else:
                prefix[i][j][k] = prefix[i-1][j][k] + prefix[i][j-1][k] - prefix[i-1][j-1][k]   

for i in range(q):
    sy,sx,ey,ex = map(int,input().split())
    ans = [0,0,0]
    for k in range(3):
        ans[k] = prefix[ey][ex][k] - prefix[ey][sx-1][k] - prefix[sy-1][ex][k] + prefix[sy-1][sx-1][k]
    print(*ans)