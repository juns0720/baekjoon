import sys
input = sys.stdin.readline

N = int(input())

dir = {0: (0,-1), 1: (1,0), 2: (0,1), 3: (-1,0)}

board = [list(map(int,input().split())) for _ in range(N)]
d = 1
res = 0
def tornado(y,x,d):
    global res
    least = 0
    #왼쪽
    if d == 0:
        for ny,nx,rate in [(y-1,x,0.07), (y-2,x,0.02), (y+1,x,0.07), (y+2,x,0.02), (y+1,x+1,0.01), (y-1,x+1,0.01), (y+1,x-1,0.1), (y-1,x-1,0.1), (y,x-2,0.05)]:
            crnt_sand = int(board[y][x]*rate)
            least += crnt_sand
            if ny < 0 or ny > N-1 or nx < 0 or nx > N-1:
                res += crnt_sand
                continue
            board[ny][nx] += crnt_sand

        least_sand = board[y][x] - least
        if x-1 < 0 or x-1 > N-1:
            res += least_sand
        else:
            board[y][x-1] += least_sand
        board[y][x] = 0

    #아래쪽
    if d == 1:
        for ny,nx,rate in [(y,x-1,0.07), (y,x-2,0.02), (y,x+1,0.07), (y,x+2,0.02), (y-1,x+1,0.01), (y-1,x-1,0.01), (y+1,x+1,0.1), (y+1,x-1,0.1), (y+2,x,0.05)]:
            crnt_sand = int(board[y][x]*rate)
            least += crnt_sand
            if ny < 0 or ny > N-1 or nx < 0 or nx > N-1:
                res += crnt_sand
                continue
            board[ny][nx] += crnt_sand

        least_sand = board[y][x] - least
        if y+1 < 0 or y+1 > N-1:
            res += least_sand
        else:
            board[y+1][x] += least_sand
        board[y][x] = 0      

    #오른쪽
    if d == 2:
        for ny,nx,rate in [(y-1,x,0.07), (y-2,x,0.02), (y+1,x,0.07), (y+2,x,0.02), (y+1,x-1,0.01), (y-1,x-1,0.01), (y+1,x+1,0.1), (y-1,x+1,0.1), (y,x+2,0.05)]:
            crnt_sand = int(board[y][x]*rate)
            least += crnt_sand
            if ny < 0 or ny > N-1 or nx < 0 or nx > N-1:
                res += crnt_sand
                continue
            board[ny][nx] += crnt_sand

        least_sand = board[y][x] - least
        if x+1 < 0 or x+1 > N-1:
            res += least_sand
        else:
            board[y][x+1] += least_sand
        board[y][x] = 0

    #위쪽
    if d == 3:
        for ny,nx,rate in [(y,x-1,0.07), (y,x-2,0.02), (y,x+1,0.07), (y,x+2,0.02), (y+1,x+1,0.01), (y+1,x-1,0.01), (y-1,x+1,0.1), (y-1,x-1,0.1), (y-2,x,0.05)]:
            crnt_sand = int(board[y][x]*rate)
            least += crnt_sand
            if ny < 0 or ny > N-1 or nx < 0 or nx > N-1:
                res += crnt_sand
                continue
            board[ny][nx] += crnt_sand

        least_sand = board[y][x] - least
        if y-1 < 0 or y-1 > N-1:
            res += least_sand
        else:
            board[y-1][x] += least_sand
        board[y][x] = 0        

y,x = N//2,N//2
cnt = 1
d = -1
t = 0
while cnt < N:
    if cnt == N-1:
        t += 1
    for i in range(2+t):
        d = (d+1) % 4
        for j in range(cnt):
            y += dir[d][0]
            x += dir[d][1]
            tornado(y,x,d)
    cnt += 1
print(res)
    