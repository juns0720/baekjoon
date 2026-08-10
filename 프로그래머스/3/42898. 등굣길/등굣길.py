def solution(m, n, puddles):

    MOD = 1000000007
    
    board = [[0 for _ in range(m)] for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    
    for x,y in puddles:
        board[y-1][x-1] = 1
        
    for y in range(n):
        if board[y][0]:
            break
        dp[y][0] = 1
        
    for x in range(m):
        if board[0][x]:
            break
        dp[0][x] = 1

    
    for y in range(1,n):
        for x in range(1,m):
            if board[y][x]:
                continue
            
            dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % MOD
    
    
    for i in dp:
        print(i)
    answer = dp[n-1][m-1]
    return answer