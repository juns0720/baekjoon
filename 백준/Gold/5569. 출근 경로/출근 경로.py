import sys
MOD = 100000

C,R = map(int,input().split())

dp = [[[[0,0], [0,0]] for _ in range(C)] for _ in range(R)]

dp[0][0][0][0] = 1
dp[0][0][1][1] = 1

# 아래 직진
for i in range(1,R):
    dp[i][0][0][0] = dp[i-1][0][0][0]

#오른쪽 직진
for i in range(1,C):
    dp[0][i][1][1] = dp[0][i-1][1][1]

def print_dp():
    for i in range(R):
        for j in range(C):
            print(dp[i][j], end = ' ')
        print()

for i in range(1,R):
    for j in range(1,C):
        dp[i][j][0][0] = (dp[i-1][j][0][0] + dp[i-1][j][1][0]) % MOD
        dp[i][j][0][1] = dp[i][j-1][0][0]
        dp[i][j][1][0] = dp[i-1][j][1][1]
        dp[i][j][1][1] = (dp[i][j-1][0][1] + dp[i][j-1][1][1]) % MOD

res = 0
for i in range(2):
    res += sum(dp[R-1][C-1][i])

print(res % MOD)