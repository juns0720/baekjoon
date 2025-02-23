import sys
input = sys.stdin.readline

'''
1. 낚시꾼이 1칸 이동한다.
2. 해당 열 가까운 상어를 잡는다.
3. 상어가 이동한다.
    3.1 한 칸에 여러 상어가 존재하면 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다. -> 이동 시 크기 max인 상어가 해당 자리 차지
4. d = [UP: 1, DOWN: 2, RIGHT: 3, REFT: 4]
'''

R,C,m = map(int,input().split())
board = [[[0,0,0] for _ in range(C)] for _ in range(R)] 
for i in range(m):
    r,c,s,d,z = map(int,input().split())
    board[r-1][c-1] = [s,d,z]

def catch(col):
    for row in range(R):
        if board[row][col][2] != 0:
            shark = board[row][col][2]
            board[row][col] = [0,0,0]
            return shark
    return 0

def left(speed, current):
    if current == 0:
        return right(speed, current)
    if speed > current:
        return right(speed-current, 0)
    else:
        return (current-speed, 4)
    
def right(speed, current):
    if current == C-1:
        return left(speed, current)
    if speed > C-current-1:
        return left(speed-((C-1)-current), C-1)
    else:
        return (current+speed, 3)
    
def up(speed, current):
    if current == 0:
        return down(speed, current)
    if speed > current:
        return down(speed-current, 0)
    else:
        return (current-speed, 1)
    
def down(speed, current):
    if current == R-1:
        return up(speed,current)
    if speed > R-current-1:
        return up(speed-((R-1)-current), R-1)
    else:
        return (current+speed, 2)

def move():
    shark_pool = [[[[0,0,0]] for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c][2] != 0:
                if board[r][c][1] == 1:
                    nr,d = up(board[r][c][0],r)
                    shark_pool[nr][c].append([board[r][c][0],d, board[r][c][2]])
                elif board[r][c][1] == 2:
                    nr,d = down(board[r][c][0],r)
                    shark_pool[nr][c].append([board[r][c][0],d, board[r][c][2]])
                elif board[r][c][1] == 3:
                    nc,d = right(board[r][c][0],c)
                    shark_pool[r][nc].append([board[r][c][0],d, board[r][c][2]])
                else:
                    nc,d = left(board[r][c][0],c)
                    shark_pool[r][nc].append([board[r][c][0],d, board[r][c][2]])
                
    for r in range(R):
        for c in range(C):
            idx, maxsize = 0,0
            for k in range(len(shark_pool[r][c])):
                if shark_pool[r][c][k][2] > maxsize:
                    idx = k
                    maxsize = shark_pool[r][c][k][2]
            board[r][c][0],board[r][c][1],board[r][c][2] = shark_pool[r][c][idx][0],shark_pool[r][c][idx][1],shark_pool[r][c][idx][2]


res = 0
for col in range(C):
    res+=catch(col) # 가까운 상어 잡기
    move()
print(res)