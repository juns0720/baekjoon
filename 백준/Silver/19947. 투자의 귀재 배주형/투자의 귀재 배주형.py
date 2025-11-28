import sys
input = sys.stdin.readline

H,Y = map(int,input().split())

dp = [0 for _ in range(Y+1)]
dp[0] = H
dp[1] = int(H*1.05)

for i in range(2,Y+1):
    dp[i] = max(int(dp[i-1]*1.05),dp[i])
    if i >= 3:
        dp[i] = max(int(dp[i-3]*1.2),dp[i])
    if i >= 5:
        dp[i] = max(int(dp[i-5]*1.35),dp[i])

print(max(dp))