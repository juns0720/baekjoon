import sys
import math
input = sys.stdin.readline

N = int(input())

dp = [N for _ in range(N+3)]
i = 1
dp[0] = 0
while i**2 <= N:
    dp[i**2] = 1
    i+=1
i = 2
while i <= N:
    max_t = int(math.sqrt(i))
    for j in range(1,max_t+1):
        dp[i] = min(dp[i],dp[i-j**2]+dp[j**2])
    i+=1
print(dp[N])

