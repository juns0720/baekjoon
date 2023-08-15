import sys
input = sys.stdin.readline

N,D = map(int,input().split())
ways = [list(map(int,input().split())) for _ in range(N)]
dp = [i for i in range(D+1)]
for i in range(0,D+1):
    if i > 0:
        dp[i] = min(dp[i],dp[i-1]+1)
    for way in ways:
        if way[0] == i and way[1] < D+1 and dp[i]+way[2] < dp[way[1]]:
            dp[way[1]] = dp[way[0]]+way[2]
print(dp[D])