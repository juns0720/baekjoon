import sys
from collections import deque
input = sys.stdin.readline

dz = [0,0,0,0,1,-1]
dy = [0,1,0,-1,0,0]
dx = [1,0,-1,0,0,0]

def bfs(end):
    while queue:
        z,y,x,dist = queue.popleft()
        if (z,y,x) == end:
            return f'Escaped in {dist} minute(s).'
        for i in range(6):
            nz = z+dz[i]
            ny = y+dy[i]
            nx = x+dx[i]
            if nz < 0 or nz > L-1 or ny < 0 or ny > R-1 or nx < 0 or nx > C-1 or \
               visited[nz][ny][nx] or matrix[nz][ny][nx] == '#':
                continue
            queue.append((nz,ny,nx,dist+1))
            visited[nz][ny][nx] = 1
    return "Trapped!"







while True:
    L,R,C = map(int,input().split())
    if L == R == C == 0:
        break

    matrix = []
    for i in range(L):
        floor = [list(input().strip()) for _ in range(R)]
        input()
        matrix.append(floor)
    
    # 시작, 도착 지점 탐색
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if matrix[i][j][k] == 'S':
                    start = (i,j,k,0)
                elif matrix[i][j][k] == 'E':
                    end =(i,j,k)
    
    queue = deque([])
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    visited[start[0]][start[1]][start[2]] = 1
    queue.append(start)

    ans = bfs(end)
    print(ans)

