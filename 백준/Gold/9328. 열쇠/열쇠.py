import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque([(0,0)])
    visited = [[0 for _ in range(C+2)] for _ in range(R+2)]
    visited[0][0] = 1
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    cnt = 0

    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny < 0 or ny > R+1 or nx < 0 or nx > C+1 or visited[ny][nx] or building[ny][nx] == '*':
                continue
            if 'A' <= building[ny][nx] <= 'Z' and building[ny][nx].lower() not in key:
                continue
            elif 'a' <= building[ny][nx] <= 'z' and building[ny][nx] not in key:
                key[building[ny][nx]] = 1
                visited = [[0 for _ in range(C+2)] for _ in range(R+2)]
            elif building[ny][nx] == '$':
                cnt+=1
                building[ny][nx] = '.'
            visited[ny][nx] = 1
            queue.append((ny,nx))
    return cnt


for tc in range(int(input())):
    R,C = map(int,input().split())
    building = [list(map(str,'.' + input().strip() + '.')) for _ in range(R)]
    building = [['.']*(C+2)] + building + [['.']*(C+2)]
    key = dict()
    for i in list(input().strip()):
        if i not in key:
            key[i] = 1
    
    print(bfs())