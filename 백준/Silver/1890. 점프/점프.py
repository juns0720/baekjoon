import sys
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)]for _ in range(N)]
dp[0][0] = 1
for y in range(N):
    for x in range(N):
        if arr[y][x] == 0:
            continue
        m = arr[y][x]
        if y+m < N:
            dp[y+m][x] += dp[y][x]
        if x+m < N:
            dp[y][x+m] += dp[y][x]
print(dp[-1][-1])