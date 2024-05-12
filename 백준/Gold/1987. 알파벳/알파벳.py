import sys
input = sys.stdin.readline

def dfs(y,x,cnt):
    global res

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if -1 < ny < R and -1 < nx < C:
            ascii = ord(board[ny][nx])
            if not visited[ascii]:
                visited[ascii] = 1
                dfs(ny,nx,cnt+1)
                res = max(cnt, res)
                visited[ascii] = 0
    res = max(cnt, res)


dy = [0,1,0,-1]
dx = [1,0,-1,0]
R,C = map(int,input().split())

board = [list(input().strip()) for _ in range(R)]
visited = [0 for _ in range(91)]
res = 0
visited[ord(board[0][0])] = 1
dfs(0,0,1)

print(res)