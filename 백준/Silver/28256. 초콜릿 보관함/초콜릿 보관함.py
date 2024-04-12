import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    cnt = 0

    while queue:
        (y,x) = queue.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if(-1 < ny < 3 and -1 < nx < 3 and box[ny][nx] =='O' and not visited[ny][nx]):
                cnt+=1
                queue.append((ny,nx))
                visited[ny][nx] = 1
    return cnt


for tc in range(int(input())):
    box = [list(input().strip()) for _ in range(3)]
    boxstatus = list(map(int,input().split()))[1:]
    counts = []

    visited = [[0 for _ in range(3)] for _ in range(3)]
    visited[1][1] = 1

    for row in range(3):
        for col in range(3):
            if not visited[row][col] and box[row][col] == 'O':
                queue = deque([])
                queue.append((row, col))
                visited[row][col] = 1
                cnt = bfs() + 1
                if (cnt > 0):
                    counts.append(cnt)
    if(len(counts) != len(boxstatus)):
        print(0)
    else:
        isSame = 1
        counts.sort(), boxstatus.sort()
        for i in range(len(counts)):
            if(counts[i] != boxstatus[i]):
                isSame = 0
        print(isSame)