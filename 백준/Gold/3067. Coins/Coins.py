import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    coins = list(map(int,input().split()))
    cost = int(input())
    
    dp = [0 for _ in range(cost+2)]
    dp[0] = 1
    for coin in coins:
        for i in range(coins[0],cost+1):
            if i-coin >=0:
                dp[i] += dp[i-coin]
    print(dp[cost])
