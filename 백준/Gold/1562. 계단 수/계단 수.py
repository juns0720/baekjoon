import sys
input = sys.stdin.readline

N = int(input())
dp = [[[0 for _ in range(2**10)] for _ in range(10)] for _ in range(N+1)]

#현재 위치 비트마스킹으로 방문처리
# 1 : 2^1, 2 : 2^2 ....
for i in range(1,10):
    dp[1][i][1<<i] = 1

for i in range(2,N+1):
    for j in range(10):
        for k in range(2**10):
            if j == 0:
                dp[i][j][k | 1<<j] += dp[i-1][j+1][k]
            elif j == 9:
                dp[i][j][k | 1<<j] += dp[i-1][j-1][k]
            else:
                dp[i][j][k | 1<<j] += (dp[i-1][j-1][k] + dp[i-1][j+1][k])

res = 0
for i in range(10):
    res += dp[N][i][2**10-1]
print(res%int(1e9))
