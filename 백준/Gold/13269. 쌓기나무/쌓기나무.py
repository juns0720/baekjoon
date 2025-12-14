import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

front = list(map(int,input().split()))
side = list(map(int,input().split()))

for i in range(N):
    for j in range(M):
        if board[i][j]:
            board[i][j] = min(side[-i-1], front[j])

for j in range(M):
    if max(board[i][j] for i in range(N)) != front[j]:
        print(-1)
        exit()

for i in range(N):
    if max(board[i]) != side[-i-1]:
        print(-1)
        exit()


for i in board:
    print(*i)