import sys
input = sys.stdin.readline

dr = [-1,0]
dc = [0,-1]
MOD = 1000007
N,M,C = map(int,input().split())

board = [[0 for _ in range(M)] for _ in range(N)]

for i in range(1,C+1):
    r,c = map(int,input().split())
    board[r-1][c-1] = i


dp = [[[[0 for _ in range(C+1)] for _ in range(C+1)] for _ in range(M)] for _ in range(N)]

if board[0][0] == 0:
    dp[0][0][board[0][0]][0] = 1
else:
    dp[0][0][board[0][0]][1] = 1



for r in range(N):
    for c in range(M):
        if (r,c) == (0,0):
            continue

        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr > N-1 or nc < 0 or nc > M-1:
                continue

            if board[r][c] == 0:
                for k in range(C+1):
                    for t in range(C+1):
                        dp[r][c][k][t] = (dp[r][c][k][t] + dp[nr][nc][k][t]) % MOD
            else:

                k = board[r][c]
                dp[r][c][k][1] = (dp[r][c][k][1]+dp[nr][nc][0][0]) % MOD

                for z in range(2,k+1):
                    for t in range(z-1,k):
                        dp[r][c][k][z] = (dp[r][c][k][z] + dp[nr][nc][t][z-1]) % MOD
                        
res = [0 for _ in range(C+1)]
for i in range(C+1):
    for j in range(C+1):
        res[j] = (res[j]+ dp[-1][-1][i][j]) % MOD
print(*res)