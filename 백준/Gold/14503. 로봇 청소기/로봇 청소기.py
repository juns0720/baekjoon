import sys
input = sys.stdin.readline

N,M = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(input().split()) for _ in range(N)]

def Cal(y,x,vec,cnt):

    if board[y][x] == '0':  #현재 위치 청소
        board[y][x] = '-1'
        cnt+=1
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    clean = True
    
    for i in range(vec+3,vec-1,-1):
        i %= 4
        ty = dy[i]+y
        tx = dx[i]+x
        if board[ty][tx] == '0':
            clean = False
            cnt = Cal(ty,tx,i,cnt)
            break
    if clean == True:
        t_vec = (vec+2)%4
        ty2 = dy[t_vec]+y
        tx2 = dx[t_vec]+x
        if board[ty2][tx2] != '1':
            cnt = Cal(ty2,tx2,vec,cnt)
    return cnt

res = Cal(r,c,d,0)
print(res)