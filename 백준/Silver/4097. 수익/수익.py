import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        exit()
    dp = [0 for _ in range(N)]
    cost = [int(input()) for _ in range(N)]
    dp[0] = cost[0]
    for i in range(1,N):
        dp[i] = max(dp[i-1] + cost[i], cost[i])
    print(max(dp))
