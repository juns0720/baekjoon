import sys
import math

INF = math.inf


idx = 1
while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int,input().split())) for _ in range(N)]
    dp = [[INF,INF,INF] for _ in range(N)]

    dp[0][0] = INF
    dp[0][1] = board[0][1]
    dp[0][2] = board[0][1] + board[0][2]

    for i in range(1,N):
        dp[i][0] = min(dp[i-1][0],dp[i-1][1]) + board[i][0]
        dp[i][1] = min(dp[i][0] ,dp[i-1][0], dp[i-1][1], dp[i-1][2]) + board[i][1]
        dp[i][2] = min(dp[i][1], dp[i-1][1], dp[i-1][2]) + board[i][2]
    print(str(idx)+'.',dp[N-1][1])
    idx+=1
