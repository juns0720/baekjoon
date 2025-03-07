import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]
MAX = min(n,m)//2



res = []

def check_size(r,c):
    max_size = 0
    for sz in range(1,MAX+1):
        make = 1
        #row
        for nr in range(r-sz,r+sz+1):
            if nr > n-1 or nr < 0 or board[nr][c] == '.':
                make = 0
                break
        if not make:
            break

        #col
        for nc in range(c-sz,c+sz+1):
            if nc > m-1 or nc < 0 or board[r][nc] == '.':
                make = 0
                break
        if not make:
            break
        max_size = sz
    return max_size

def make(r,c,size):
    #row
    for nr in range(r-size,r+size+1):
            if nr < 0 or nr > n-1:
                continue
            board[nr][c] = '.'

    #col
    for nc in range(c-size,c+size+1):
        if nc < 0 or nc > m-1:
            continue
        board[r][nc] = '.'
for r in range(n):
    for c in range(m):
        if board[r][c] == '*':
            size = check_size(r,c)
            if size:
                res.append((r,c,size))
for i in res:
    make(i[0],i[1],i[2])

for r in range(n):
    for c in range(m):
        if board[r][c] == '*':
            print(-1)
            exit()
length = len(res)
if length > n*m:
    print(-1)
else:
    print(length)
    for i in res:
        print(i[0]+1, i[1]+1, i[2])