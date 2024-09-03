import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
M = int(input())
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(0, N-1):
    if lst[i] == lst[i+1]:
        dp[i][i+1] = 1

for i in range(N-1,-1,-1):
    for j in range(i+2,N):
        if lst[i] == lst[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

for i in range(M):
    s,e = map(int,input().split())
    print(dp[s-1][e-1])
