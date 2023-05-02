import sys
input = sys.stdin.readline

N,M = map(int,input().split())
al = list(map(int,input().split()))
dp = [0 for i in range(N+3)]
t = 1
while t <= N:
    dp[t] = dp[t-1]+al[t-1]
    t+=1
for _ in range(M):
    i,j = map(int,input().split())
    if i == 1:
        print(dp[j])
    else:
        print(dp[j]-dp[i-1])
