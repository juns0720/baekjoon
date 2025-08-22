import sys
input = sys.stdin.readline

dx = [-1,0,1]

INF = sys.maxsize

N,M = map(int,input().split())
cost = [list(map(int,input().split())) for _ in range(N)]


dp = [[[INF,INF,INF] for _ in range(M)] for _ in range(N)]

for i in range(M):
    for d in range(3):
        dp[0][i][d] = cost[0][i]


for y in range(1,N):
    for x in range(M):
        for pd in range(3):
            for nd in range(3):
                px = x + dx[nd]
                if px < 0 or px > M-1 or pd == nd:
                    continue
                dp[y][x][nd] = min(dp[y][x][nd], dp[y-1][px][pd] + cost[y][x])

res = INF
for i in dp[-1]:
    res = min(res,min(i))
print(res)