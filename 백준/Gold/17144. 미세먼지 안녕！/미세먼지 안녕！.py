import sys
input = sys.stdin.readline

R,C,T = map(int,input().split())
board = [[[0,0] for _ in range(C)] for _ in range(R)]

air_pos = []

for row in range(R):
    tmp = list(map(int,input().split()))
    for col in range(C):
        if tmp[col] == -1:
            air_pos.append((row,col))
        board[row][col][0] = tmp[col]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def diffusion():
    for y in range(R):
        for x in range(C):
            if board[y][x][0] < 5:
                continue
            else:
                dif_dust = board[y][x][0] // 5
                for i in range(4):
                    ny = y+dy[i]
                    nx = x+dx[i]
                    if ny < 0 or ny > R-1 or nx < 0 or nx > C-1:
                        continue
                    if board[ny][nx][0] == -1:
                        continue
                    else:
                        board[ny][nx][1] += dif_dust
                        board[y][x][0] -= dif_dust
    board_reset()

def board_reset():
    for row in range(R):
        for col in range(C):
            board[row][col][0], board[row][col][1] = sum(board[row][col]), 0

def top_curculation():
    (y,x) = air_pos[0]

    #왼쪽 
    for dy in range(y-1,0,-1):
        board[dy][0][0] = board[dy-1][0][0]
    board[0][0][0] = 0
    #위쪽
    for dx in range(C-1):
        board[0][dx][0] = board[0][dx+1][0]
    board[0][C-1][0] = 0
    #오른쪽
    for dy in range(y):
        board[dy][C-1][0] = board[dy+1][C-1][0]
    board[y][C-1][0] = 0
    #아래
    for dx in range(C-1,0,-1):
        board[y][dx][0] = board[y][dx-1][0]
    board[y][1][0] = 0

def bottom_curculation():
    (y,x) = air_pos[1]
    
    #왼쪽
    for dy in range(y+1,R-1):
        board[dy][0][0] = board[dy+1][0][0]
    board[R-1][0][0] = 0
    #아래쪽
    for dx in range(C-1):
        board[R-1][dx][0] = board[R-1][dx+1][0]
    board[R-1][C-1][0] = 0
    #오른쪽 
    for dy in range(R-1,y,-1):
        board[dy][C-1][0] = board[dy-1][C-1][0]
    board[y][C-1][0] = 0
    #위쪽
    for dx in range(C-1,1,-1):
        board[y][dx][0] = board[y][dx-1][0]
    board[y][1][0] = 0

for _ in range(T):
    diffusion()
    top_curculation()
    bottom_curculation()

res = 2
for row in range(R):
    for col in range(C):
        res+= board[row][col][0]
print(res)