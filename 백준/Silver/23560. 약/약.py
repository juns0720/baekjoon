import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n)]
dp[0] = 2

for i in range(1,n):
    dp[i] = dp[i-1]*3

print(dp[n-1])