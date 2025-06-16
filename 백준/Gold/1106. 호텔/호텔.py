import sys
input = sys.stdin.readline

C,n = map(int,input().split())
MAX_SIZE = C+100
INF = sys.maxsize
dp = [INF for _ in range(MAX_SIZE+1)]

dp[0] = 0

for _ in range(n):
    cost,weight = map(int,input().split())
    dp[weight] = min(dp[weight], cost)
    for i in range(weight, MAX_SIZE):
        if i-weight > 0:
            dp[i] = min(dp[i], dp[i-weight]+cost)
print(min(dp[C:]))