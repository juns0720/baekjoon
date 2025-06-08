import sys
input = sys.stdin.readline
INF = sys.maxsize
d,p = map(int,input().split())

pipe = [list(map(int,input().split())) for _ in range(p)]

dp = [0 for _ in range(d+1)]
dp[0] = INF

for i in range(p):
    for length in range(d,pipe[i][0]-1,-1):
            dp[length] = max(dp[length], min(dp[length-pipe[i][0]],pipe[i][1]))
print(dp[d])