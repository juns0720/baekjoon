import sys
input = sys.stdin.readline

T = int(input())
dp = [[0 for _ in range(15)] for _ in range(15)]
for _ in range(T):
    k = int(input())
    n = int(input())
    for i in range(1,n+1):
        dp[0][i] = i
    for i in range(1,k+1):
        for j in range(1,n+1):
            if dp[i][j] == 0:
                for t in range(1,j+1):
                        dp[i][j]+= dp[i-1][t]
    print(dp[k][n])
