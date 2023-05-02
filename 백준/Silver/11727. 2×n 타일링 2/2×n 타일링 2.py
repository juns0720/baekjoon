import sys
input = sys.stdin.readline
N = int(input())
dp = [0 for i in range(N+3)]


dp[1] = 1
dp[2] = 3
dp[3] = 5

i = 4
while N >= i:
    if i % 2 == 0:
        dp[i] = dp[i-1]*2+1
    else:
        dp[i] = dp[i-1]*2-1
    i+=1
print(dp[N]%10007)