import sys

board = [list(map(int,input().split())) for _ in range(5)]
r,c = map(int,input().split())
dy = [1,0,-1,0]
dx = [0,1,0,-1]
def dfs(y, x, depth, cnt):
    if depth < 4 and cnt > 1:
            print(1)
            exit()
    if depth > 3:
        return


    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if -1 < ny < 5 and -1 < nx < 5:
            if board[ny][nx] != -1:
                if board[ny][nx] == 1:
                    board[ny][nx] = -1
                    dfs(ny,nx,depth+1, cnt+1)
                    board[ny][nx] = 1
                else:
                    board[ny][nx] = -1
                    dfs(ny,nx,depth+1, cnt)
                    board[ny][nx] = 0
            


board[r][c] = -1
dfs(r,c, 0, 0)
print(0)