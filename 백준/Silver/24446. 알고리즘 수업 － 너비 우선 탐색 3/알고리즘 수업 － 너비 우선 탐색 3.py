import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]


def bfs():
    while queue:
        v1,depth = queue.popleft()
        res[v1] = depth
        for v2 in graph[v1]:
            if visited[v2]:
                continue
            queue.append((v2,depth+1))
            visited[v2] = 1

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]
res = [-1 for _ in range(n+1)]
queue = deque([(r,0)])
visited[r] = 1
bfs()
for i in res[1:]:
    print(i)