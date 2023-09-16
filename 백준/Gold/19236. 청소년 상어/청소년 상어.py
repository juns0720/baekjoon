import sys
from copy import deepcopy
input = sys.stdin.readline

board = []
for i in range(4):
    tmp = list(map(int,input().split()))
    board.append([[tmp[0],tmp[1]-1],[tmp[2],tmp[3]-1],[tmp[4],tmp[5]-1],[tmp[6],tmp[7]-1]])

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]

def shark_move(board,sy,sx,sum):
    global res
    sum +=board[sy][sx][0]
    svec = board[sy][sx][1]
    board[sy][sx][0] = -1
    res = max(res,sum)

    for fish in range(1,17):
        flag2 = True
        for y in range(4):
            if not flag2:
                break
            for x in range(4):
                if board[y][x][0] == -1 or board[y][x][0] == 0:
                    continue
                elif board[y][x][0] == fish: #물고기 위치 변경하기
                    flag2 = False
                    for i in range(board[y][x][1],board[y][x][1]+7):
                        ty,tx = y+dy[i%8], x+dx[i%8]    # 이동할 위치
                        if -1 < ty < 4 and -1 < tx < 4 and board[ty][tx][0] != -1:
                            board[y][x][1] = i%8
                            board[y][x][0],board[ty][tx][0] = board[ty][tx][0],board[y][x][0]
                            board[y][x][1],board[ty][tx][1] = board[ty][tx][1],board[y][x][1]
                            break
                    break
    for i in range(1,4):
        ty,tx = sy+dy[svec]*i, sx+dx[svec]*i
        if -1 < ty < 4 and -1 < tx < 4 and board[ty][tx][0] != 0:
            board[sy][sx][0] = 0
            shark_move(deepcopy(board),ty,tx,sum)

#초기 상어위치 설정
res = 0
shark_move(deepcopy(board),0,0,0)
print(res)