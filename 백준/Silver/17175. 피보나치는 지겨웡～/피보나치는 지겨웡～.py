import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+3)]

dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2] + 1
print(dp[n] % 1000000007)
