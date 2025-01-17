import sys
input = sys.stdin.readline

N = int(input())

time = [list(map(int,input().split())) for _ in range(N)]


dp = [0 for _ in range(N)]
dp[0] = time[0][2]
for i in range(1,N):
    dp[i] = max(dp[i-1],dp[i-2]+time[i][2])
print(dp[N-1])