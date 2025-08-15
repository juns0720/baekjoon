import sys
input = sys.stdin.readline

N = int(input())

arr = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(N):
    arr.append(list(map(int,input().split())))

dp = [0 for _ in range(N+3)]

for i in range(3,N+3):
    dp[i] = max(dp[i-2], dp[i-3]) + arr[i][2]

print(max(dp[-1],dp[-2]))