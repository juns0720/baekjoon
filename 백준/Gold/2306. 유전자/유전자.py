import sys
input = sys.stdin.readline

s1 = ["0"] + list(input().strip())
length = len(s1)-1
dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s1)+1)]
KOI = ['at','gc']

#길이가 2인 KOI 유전자
for l in range(2,length+1):
    for e in range(l,length+1):
        s = e-l+1
        if s1[s]+s1[e] in KOI:
            dp[s][e] = 2
            dp[e][s] = 2

#KOI 유전자 조합
for l in range(3,length+1):
    for e in range(l,length+1):
        s = e-l+1
        if s1[s]+s1[e] in KOI:
            max_len = dp[s+1][e-1]
            for k in range(s+1,e-1):
                max_len = max(max_len,dp[s+1][k] + dp[k+1][e-1])
            dp[s][e] = max(dp[s][e],max_len+2)
        for k in range(s,e):
            dp[s][e] = max(dp[s][e], dp[s][k] + dp[k+1][e])
res = 0
for i in range(length+1):
    for j in range(length+1):
        res = max(res,dp[i][j])
print(res)
