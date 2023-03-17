import sys
input = sys.stdin.readline

n = int(input())
stair = []
for i in range(n):
    stair.append(int(input()))

Dp = [0 for i in range(n)]
if n > 2:
    Dp[0] = stair[0]
    Dp[1] = stair[0]+stair[1]
    Dp[2] = max(stair[0] +stair[2], stair[1] + stair[2])
elif n == 1:
    Dp[0] = stair[0]
elif n == 2:
    Dp[1] = stair[0]+stair[1]

for i in range(3,n):
    Dp[i] = max(Dp[i-2] + stair[i],Dp[i-3]+stair[i-1]+stair[i])
print(Dp[n-1])
      



