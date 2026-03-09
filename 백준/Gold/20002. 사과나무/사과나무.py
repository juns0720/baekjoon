import sys
input = sys.stdin.readline

N = int(input())
INF = sys.maxsize

board = [[0 for _ in range(N+1)]]+[[0] + list(map(int,input().split())) for _ in range(N)]
prefix = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] + board[i][j] - prefix[i-1][j-1]

res = -INF
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(min(i,j),0,-1):
            res = max(res, prefix[i][j] - prefix[i][j-k] - prefix[i-k][j] + prefix[i-k][j-k])

print(res)