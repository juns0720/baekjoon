import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [0 for i in range(n+3)]
for i in range(1,math.floor((math.sqrt(n)))+1):
    dp[i**2] = 1
dp[2] = dp[1]+1
dp[3] = dp[2]+1
j = 3

if n > 3:
    while True: 
        j+=1
        max_s = math.floor((math.sqrt(j)))
        if dp[j] != 1:
            for i in range(max_s+1):
                if dp[j] == 0:
                    dp[j] = min(dp[j-1]+1,dp[j-i**2]+dp[i**2])
                    if dp[j] == 2:
                        break
                else:
                    dp[j] = min(dp[j],dp[j-1]+1,dp[j-i**2]+dp[i**2])
                    if dp[j] == 2:
                        break
                    
        if j == n:
            break
print(dp[n])

    
