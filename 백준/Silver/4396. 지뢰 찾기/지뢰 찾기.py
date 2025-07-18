import sys
input = sys.stdin.readline

dy = [-1,-1,-1,0,0,0,1,1,1]
dx = [-1,0,1,-1,0,1,-1,0,1]

N = int(input())
board1 = [list(input().strip()) for _ in range(N)]
board2 = [list(input().strip()) for _ in range(N)]

def find(y,x):
    cnt = 0
    for i in range(9):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny > N-1 or nx < 0 or nx > N-1 or board1[ny][nx] == '.':
            continue
        cnt += 1
    return cnt

res = [['.' for _ in range(N)] for _ in range(N)]

def fail():
    for r in range(N):
        for c in range(N):
            if board1[r][c] == '*':
                res[r][c] = '*'
flag = 0
for r in range(N):
    for c in range(N):
        if board2[r][c] == 'x':
            if board1[r][c] == '*':
                flag = 1
            else:
                res[r][c] = find(r,c)
if flag:
    fail()
for i in res:
    for s in i:
        print(s, end = '')
    print()