import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]
fivo = [0 for _ in range(n+1)]
fivo[1] = 0
fivo[2] = 1

dp[1] = 1
dp[2] = 2

cnt = 1
for i in range(3,n+1):
    fivo[i] = (fivo[i-1] + fivo[i-2]) % 10
    dp[i] += (fivo[i]+dp[i-1]) % 10


print(dp[n])