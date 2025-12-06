import sys
input = sys.stdin.readline

R,C = map(int,input().split())

board = [[' ' for _ in range(C+1)]] + [[' '] + list(input().strip()) for _ in range(R)]

#세로, 가로
prefix = [[[0,0] for _ in range(C+1)] for _ in range(R+1)]

for r in range(1,R+1):
    for c in range(1,C+1):
        if board[r][c] == '.':
            prefix[r][c][0] = prefix[r-1][c][0] + 1
            prefix[r][c][1] = prefix[r][c-1][1] + 1

max_size = 0
for r in range(1,R+1):
    for c in range(1,C+1):
        size = [
            max_size,
            prefix[r][c][0]*2 + 2 if prefix[r][c][0] != 0 else 0,
            prefix[r][c][1]*2 + 2 if prefix[r][c][1] != 0 else 0
                ]
        
        nr, nc = prefix[r][c][0], prefix[r][c][1]

        for r2 in range(r,r-prefix[r][c][0], -1):
            nc = min(prefix[r2][c][1], nc)
        size.append((nc+prefix[r][c][0])*2)

        for c2 in range(c,c-prefix[r][c][1], -1):
            nr = min(prefix[r][c2][0], nr)
        size.append((nr+prefix[r][c][1])*2)
        
        max_size = max(size)
print(max(max_size-1, 0))