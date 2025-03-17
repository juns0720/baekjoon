import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

visited = [[0 for _ in range(n*3)] for _ in range(2)]
res = 0
def check(y,x,cnt):
    global ans

    if n % 2:
        if x == n:
            y += 1
            x = 0
        elif x == n+1:
            y += 1
            x = 1
    else:
        if x == n:
            y += 1
            x = 1
        elif x == n+1:
            y += 1
            x = 0
    
    if y == n:
        if ans < cnt:
            ans = cnt
        return
    
    if board[y][x] == 1 and not visited[0][y+x] and not visited[1][y-x]:
        visited[0][y+x] = 1
        visited[1][y-x] = 1
        check(y, x+2, cnt+1)
        visited[0][y+x] = 0
        visited[1][y-x] = 0

    check(y, x+2, cnt)
ans = 0
check(0,0,0)
res += ans
ans = 0
check(0,1,0)
print(res + ans)