import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    sy,sx = queue[0]
    cnt = 1
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 < ny < 5 and -1 < nx < width and signer[ny][nx] =='#' and not visited[ny][nx]:
                queue.append((ny,nx))
                visited[ny][nx] = 1
                cnt+=1
    if cnt == 5:
        return 1
    elif cnt == 7:
        return 7
    elif cnt == 9:
        return 4
    elif cnt == 11:
        if signer[sy+1][sx+2] == '.':
            return 5
        elif signer[sy+3][sx] =='.':
            return 3
        else:
            return 2
    elif cnt == 12:
        if signer[sy+1][sx+2] == '.':
            return 6
        elif signer[sy+3][sx] == '.':
            return 9
        else:
            return 0
    elif cnt == 13:
        return 8




len_signer = int(input())
width = len_signer // 5
tmp_signer = input().strip()
queue = deque([])
visited = [[0 for _ in range(width)] for _ in range(5)]
signer = []
for i in range(5):
    signer.append(tmp_signer[width*i : width*(i+1)])


col = 0
for i in range(width):
    if signer[0][i] == '#' and not visited[0][i]:
        queue.append((0,i))
        visited[0][i] = 1
        print(bfs(), end='')



        
        

