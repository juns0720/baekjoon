import sys
input = sys.stdin.readline

k, n = map(int, input().split())
if k == 0:
    print(0)
    exit()

MAXD = k + n + 2 

dp = [[0] * (n + 1) for _ in range(MAXD)]

for d in range(1, MAXD):
    dp[d][0] = 1
dp[0][0] = 0

for t in range(1, n + 1):
    dp[0][t] = 0  
    for d in range(1, MAXD - 1):
        dp[d][t] = dp[d - 1][t - 1] + dp[d + 1][t - 1]

print(dp[k][n])