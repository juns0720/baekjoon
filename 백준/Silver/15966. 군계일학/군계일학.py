import sys
input = sys.stdin.readline

N = int(input())
dp = [1 for _ in range(N+1)]
arr = list(map(int,input().split()))

for i in range(N):
    for j in range(i+1, N):
        if arr[j] == arr[i]+1:
            dp[j] = max(dp[j], dp[i]+1)
print(max(dp))