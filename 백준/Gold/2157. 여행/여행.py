import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

cost = [[-1 for _ in range(n+1)] for _ in range(n+1)]
pos = {}
for _ in range(k):
    v1,v2,c = map(int,input().split())
    if v1 > v2:
        continue
    cost[v1][v2] = max(cost[v1][v2],c)

dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

for i in range(m+1):
    dp[1][i] = 0
for v1 in range(1, n+1):
    for v2 in range(v1+1,n+1):
        if cost[v1][v2] == -1:
            continue
        for cnt in range(1,m):
            if dp[v1][cnt] == -1:
                continue
            dp[v2][cnt+1] = max(dp[v2][cnt+1], dp[v1][cnt] + cost[v1][v2])
res = max(dp[n])

if res == -1:
    print(0)
else:
    print(res)
    