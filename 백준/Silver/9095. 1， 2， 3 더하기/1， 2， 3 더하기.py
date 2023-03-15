import sys
input = sys.stdin.readline


k = int(input())
Dp = [0 for i in range(12)]
Dp[0],Dp[1],Dp[2] = 1,2,4


for j in range(k):
    n = int(input())
    for i in range(n):
        if (i > 2):
            Dp[i] = Dp[i-1]+Dp[i-2]+Dp[i-3]
    print(Dp[i])
