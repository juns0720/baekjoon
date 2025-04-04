import sys
input = sys.stdin.readline


lst = list(map(int,str(input().strip())))

dp = [[0,0] for _ in range(len(lst)+1)]

n = len(lst)

if lst[0] != 0:
    dp[1][0] = 1
else:
    dp[1][0] = 0
dp[1][1] = 0


for i in range(2,n+1):
    if lst[i-1] != 0:
        dp[i][0] = dp[i-1][0] + dp[i-1][1]

    if (0 < lst[i-2]*10+lst[i-1] < 35):
        dp[i][1] = dp[i-1][0]
        
print(sum(dp[n]))