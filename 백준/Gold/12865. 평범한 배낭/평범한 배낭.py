import sys
input = sys.stdin.readline

n,k = map(int,input().split())
item = [0]+[list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for cur_weight in range(k+1):
        if cur_weight < item[i][0]:
            dp[i][cur_weight] = dp[i-1][cur_weight]
        else:
            dp[i][cur_weight] = max(dp[i-1][cur_weight-item[i][0]] + item[i][1], dp[i-1][cur_weight])

print(dp[-1][-1])