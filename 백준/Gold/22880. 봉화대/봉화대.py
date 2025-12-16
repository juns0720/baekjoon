import sys
input = sys.stdin.readline

MOD = 1000000007
n = int(input())
heights = list(map(int,input().split()))

prev = heights[0]

arr = []
cnt = 1
for i in range(1, n):
    if heights[i] > prev:
        arr.append(cnt)
        cnt = 1
        prev = heights[i]
    else:
        cnt += 1
if not arr:
    print(1)
    exit()
dp = [0 for _ in range(len(arr))]

dp[0] = arr[0]
for i in range(1,len(arr)):
    dp[i] = ((dp[i-1]*arr[i]) + dp[i-1]+arr[i]) % MOD
print((dp[-1]+1) % MOD)