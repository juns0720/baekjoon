import sys
input = sys.stdin.readline

R,C = map(int,input().split())
board = [list(input().strip()) for _ in range(R)]

for r in range(R):
    for c in range(C):
        if board[r][c] == '.':
            continue
        board[r][C-1-c] = board[r][c]
        
for i in board:
    print(*i, sep = '')