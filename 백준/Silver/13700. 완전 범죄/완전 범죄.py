import sys
from collections import deque
input = sys.stdin.readline

n,s,d,f,b,k = map(int,input().split())
police = list(map(int,input().split()))

def bfs():
    visited = [0 for _ in range(n+1)]
    queue = deque([])
    queue.append((s,0))
    visited[s] = 1
    dx = [f,-b]

    while queue:
        x, dist = queue.popleft()
        if x == d:
            print(dist)
            exit(0)
        for i in range(2):
            nx = x+dx[i]
            if 0 < nx < n+1 and not visited[nx] and nx not in police:
                queue.append((nx,dist+1))
                visited[nx] = 1
bfs()
print("BUG FOUND")