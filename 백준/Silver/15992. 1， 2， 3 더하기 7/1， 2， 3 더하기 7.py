import sys
input = sys.stdin.readline
MOD = 1000000009
dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[1][1] = 1
dp[2][1], dp[2][2] = 1, 1
dp[3][1],dp[3][2], dp[3][3] = 1, 2, 1

for i in range(4, 1001):
    for j in range(1,i+1):
        for k in range(1,4):
            if i-k < j-1:
                continue
            dp[i][j] = (dp[i][j] + dp[i-k][j-1]) % MOD

for tc in range(int(input())):
    n,m = map(int,input().split())
    print(dp[n][m])