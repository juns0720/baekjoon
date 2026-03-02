import sys
input = sys.stdin.readline

MAX = 0

N,T = map(int,input().split())

items = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]

for i in items:
    MAX  += i[1]

dp = [[0 for _ in range(T+1)] for _ in range(N+1)]
for i in range(T+1):
    dp[0][i] = MAX

for i in range(1,N+1):
    weight,cost = items[i]
    for j in range(T+1):
        if j - weight < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-weight] - cost, dp[i][j-1])

print(dp[-1][-1])