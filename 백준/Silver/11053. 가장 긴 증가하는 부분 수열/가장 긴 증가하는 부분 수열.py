import sys
input = sys.stdin.readline


n = int(input())
dp = [1 for i in range(n)]
a = list(map(int,input().split()))

for i in range(1,n):
    for j in range(0, i):
        if a[i] > a[j]:
            dp[i] = max(dp[i],dp[j]+1)
    
print(max(dp))



        