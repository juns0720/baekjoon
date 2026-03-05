import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().strip())) for _ in range(N)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]
dr2 = [1,1,-1,-1]
dc2 = [-1,1,-1,1]


def isPlus(r,c,l):


    for i in range(4):
        nr = r + dr[i]*l
        nc = c + dc[i]*l

        #플러스 검사
        if nr < 0 or nr > N-1 or nc < 0 or nc > N-1 or not board[nr][nc]:
            return 0
        
        nnr = r + dr2[i]*l
        nnc = c + dc2[i]*l

        #모서리 0 검사
        if nnr < 0 or nnr > N-1 or nnc < 0 or nnc > N-1 or board[nnr][nnc]:
            return 0

    #네모 박스 0 검사
    for nr in [r-l, r+l]:
        for i in range(1,l):
            if board[nr][c-i] or board[nr][c+i]:
                return 0
            
    for nc in [c-l, c+l]:
        for i in range(1,l):
            if board[r-i][nc] or board[r+i][nc]:
                return 0
        
    return 1

res = 0
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            l = 1

            while isPlus(r,c,l):
                res += 1
                l += 1

print(res)