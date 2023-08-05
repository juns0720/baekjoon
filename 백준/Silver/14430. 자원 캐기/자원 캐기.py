import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(input().split()) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = int(board[0][0])
for y in range(N):
    for x in range(M):
        if y-1 > -1:
            dp[y][x] = max(dp[y-1][x] + int(board[y][x]),dp[y][x])
        if x-1 > -1:
            dp[y][x] = max(dp[y][x-1] + int(board[y][x]),dp[y][x])
print(dp[N-1][M-1])