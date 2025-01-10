import sys
input = sys.stdin.readline

N,K = map(int,input().split())

dp = [[0 for _ in range(201)] for _ in range(201)]
for i in range(201):
    dp[0][i] = 1
    dp[1][i] =i

for i in range(2,201):
    for j in range(1,201):
        prev = 0
        for z in range(i-1,-1,-1):
            prev+=dp[z][j-1]
        dp[i][j] = (dp[i][j-1] + prev) % 1000000000
print(dp[N][K])