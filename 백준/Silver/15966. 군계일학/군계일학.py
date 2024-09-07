import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(10**6+1)]
arr = [0]+list(map(int,input().split()))
for i in range(1,N+1):
    num = arr[i]
    dp[num] = max(dp[num], dp[num-1]+1)
print(max(dp))