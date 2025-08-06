import sys
input = sys.stdin.readline
N = int(input())

dp = [0 for _ in range(N+3)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,N+1):
    dp[i] = dp[i-1]*2
    if i % 2 == 0:
        for j in range(i,i-5,-1):
            dp[j] -= dp[i-4]
        for j in range(i,i-4,-1):
            dp[j] -= dp[i-3]

print(dp[N])