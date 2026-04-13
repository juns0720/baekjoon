import sys
input = sys.stdin.readline

num = list(map(int,input().strip()))
n = len(num)
dp = [[0,0] for _ in range(n)]

MOD  = 1000000

if num[0] > 0:
    dp[0][0] = 1

for i in range(1,n):
    if num[i] == 0:
        if num[i-1] in [1,2]:
            dp[i][1] = dp[i-1][0]
        continue

    if num[i-1] == 0:
        dp[i][0] = dp[i-1][1]
        continue

    if num[i-1] == 1:
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]

    elif num[i-1] == 2:
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        if num[i] <= 6:
            dp[i][1] = dp[i-1][0]

    elif num[i-1] not in [1,2]:
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
    
    dp[i][0] %= MOD
    dp[i][1] %= MOD


print(sum(dp[-1])%MOD)
