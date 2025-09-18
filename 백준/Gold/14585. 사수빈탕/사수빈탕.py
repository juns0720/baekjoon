import sys
input = sys.stdin.readline
n,m = map(int,input().split())
MAX_SIZE = 301

board = [[0 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]
for _ in range(n):
    y,x = map(int,input().split())
    board[y][x] = m

dp = [[-1 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]
dp[0][0] = 0

for y in range(MAX_SIZE):
    for x in range(MAX_SIZE):
        if (y,x) == (0,0):
            continue
        cost = -1

        if y > 0:
            cost = max(cost, dp[y-1][x])
        if x > 0:
            cost = max(cost, dp[y][x-1])
            
        cost += max(0,board[y][x]-(x+y))
        dp[y][x] = max(dp[y][x], cost)

print(dp[MAX_SIZE-1][MAX_SIZE-1])
