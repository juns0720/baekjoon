def solution(n):
    dp = [0 for _ in range(n+2)]
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n+2):
        dp[i] = (dp[i-1]+dp[i-2])%1234567
    return dp[n+1]
