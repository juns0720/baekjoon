import sys
input = sys.stdin.readline

N = int(input())
dp = [[0,0,0,0,0,0,0,0,0,0] for _ in range(N+2)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]
dp[2] = [1,1,2,2,2,2,2,2,2,1]

for i in range(3,N+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
print(sum(dp[N])%int(1e9))