import sys
input = sys.stdin.readline

n,m = map(int,input().split())
MOD = 1000000007
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][1] = 1
for i in range(1,m+1):
    dp[1][i] = 1

for i in range(2,n+1):
    for j in range(2,m+1):
        dp[i][j] = max(dp[i][j],dp[i-1][j-1]+dp[i][j-1]+dp[i-1][j])


print(dp[n][m]%MOD)