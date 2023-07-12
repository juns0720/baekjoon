import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    field = []
    visited = [False for _ in range(n+3)]
    queue = deque([])
    for _ in range(n+2):
        x,y = map(int,input().split())
        field.append((x,y))
    def move(now,n):
        visited[now] = True
        queue.append(field[now])
        while queue:
            if visited[n+1] == True:
                return
            x,y = queue.popleft()
            for i in range(now,n+2):
                if visited[i] != True:
                    nx = field[i][0]
                    ny = field[i][1]
                    dis = abs(x-nx)+ abs(y-ny)
                    if dis <= 1000:
                        visited[i] = True             
                        queue.append((nx,ny))
    move(0,n)
    if visited[n+1] == True:
        print('happy')
    else:
        print('sad')

