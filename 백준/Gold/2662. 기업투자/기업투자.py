import sys
input = sys.stdin.readline

n,m = map(int,input().split())

money = [[0 for _ in range(n+1)] for _ in range(m)]

for i in range(n):
    c = list(map(int,input().split()))
    for j in range(m):
        money[j][c[0]] = c[j+1]
dp = [[[0,0,0] for _ in range(n+1)] for _ in range(m)]
dp[0][0][1] = -1
for i in range(1,n+1):
    dp[0][i] = [money[0][i],-1,i]

for i in range(1,m):
    for cost in range(n+1):
        dp[i][cost] = [dp[i-1][cost][0], i-1,0]
        for curr_cost in range(cost+1):

            if dp[i-1][cost][0] < dp[i-1][cost-curr_cost][0] + money[i][curr_cost]:
                if dp[i][cost][0] >= dp[i-1][cost-curr_cost][0] + money[i][curr_cost]:
                    continue
                dp[i][cost][0] = dp[i-1][cost-curr_cost][0] + money[i][curr_cost]
                dp[i][cost][2] = curr_cost

v = m-1
c = n
res = [dp[v][c][2]]
while v > 0:
    c -= dp[v][c][2]
    v -= 1
    res.append(dp[v][c][2])

print(dp[m-1][n][0])
print(*list(reversed(res)))