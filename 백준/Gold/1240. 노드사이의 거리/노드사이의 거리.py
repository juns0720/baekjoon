import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for i in range(N-1):
    v1,v2,c = map(int,input().split())
    graph[v1].append((v2,c))
    graph[v2].append((v1,c))

def bfs(s,e):
    queue = deque([(s,0)])
    visited = [0 for _ in range(N+1)]
    visited[s] = 1

    while queue:
        v1,c1 = queue.popleft()

        if v1 == e:
            return c1

        for v2,c2 in graph[v1]:
            if visited[v2]:
                continue

            queue.append((v2,c1+c2))
            visited[v2] = 1


for i in range(M):
    v1,v2 = map(int,input().split())
    print(bfs(v1,v2))