import sys
input = sys.stdin.readline

s1 = list(input().strip())
l = len(s1)
p = [[0 for _ in range(l)] for _ in range(l)]

for i in range(l):
    p[i][i] = 1

for i in range(1,len(s1)):
    if s1[i-1] == s1[i]:
        p[i-1][i] = 1

for i in range(3,l+1):
    for s in range(l-i+1):
        e = s+i-1
        if s1[s] == s1[e] and p[s+1][e-1] == 1:
            p[s][e] = 1

dp = [2500 for _ in range(l+1)]
dp[-1] = 0
for e in range(l):
    for s in range(e+1):
        if p[s][e]:
            dp[e] = min(dp[e], dp[s-1]+1)
        else:
            dp[e] = min(dp[e], dp[e-1]+1)
print(dp[l-1])
