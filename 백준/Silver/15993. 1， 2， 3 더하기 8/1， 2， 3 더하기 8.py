import sys
input = sys.stdin.readline

# 0 = 홀, 1 = 짝
MOD = 1000000009
dp = [[0,0] for _ in range(100001)]
dp[1][0] = 1
dp[2][0],dp[2][1] = 1,1
dp[3][0],dp[3][1] = 2,2
for i in range(4,100001):
    dp[i][0] = (dp[i-1][1] + dp[i-2][1] + dp[i-3][1]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][0]) % MOD
for i in range(int(input())):
    print(*dp[int(input())])

