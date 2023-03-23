import sys
input = sys.stdin.readline

n = int(input())
grape = [int(input()) for i in range(n)]
dp = [0 for i in range(n+1)]

dp[0] = grape[0]
if n > 1:
    dp[1] = dp[0]+grape[1]
if n > 2:   
    dp[2] = max(dp[0] + grape[2],grape[1] + grape[2],dp[1])

if n < 4:
    print(max(dp))
else:
    i = 3
    while True:
        dp[i] = max(dp[i-2] + grape[i], dp[i-3] + grape[i-1]+grape[i],dp[i-1])
        if i == n-1:
            break
        else:
            i+=1
    print(max(dp))