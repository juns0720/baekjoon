import sys
import math
input = sys.stdin.readline
INF = math.inf


N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]


res = INF
for i in range(3):
    dp = [[INF,INF,INF] for _ in range(N)]
    for j in range(3):
        dp[0][i] = house[0][i]
    dp[1][(i+1)%3] = dp[0][i]+house[1][(i+1)%3]
    dp[1][(i+2)%3] = dp[0][i]+house[1][(i+2)%3]
    for j in range(2,N):
        for k in range(3):
            if j == N-1 and i == k:
                continue
            dp[j][k] = min(dp[j][k], dp[j-1][(k+1)%3]+house[j][k], dp[j-1][(k+2)%3]+house[j][k])
    res = min(res, min(dp[-1]))
print(res)
