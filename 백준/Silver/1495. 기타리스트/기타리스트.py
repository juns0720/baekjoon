import sys
input = sys.stdin.readline

n,s,m = map(int,input().split())
v = [0]+list(map(int,input().split()))
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

dp[0][s] = 1

for i in range(1,n+1):
    for p in range(m+1):
        if dp[i-1][p] == 1:
            vol = [p+v[i], p-v[i]]
            if -1 < p+v[i] < m+1:
                dp[i][p+v[i]] = 1
            if -1 < p-v[i] < m+1:
                dp[i][p-v[i]] = 1

for vol in range(m,-1,-1):
    if dp[-1][vol] == 1:
        print(vol)
        exit()
print(-1)