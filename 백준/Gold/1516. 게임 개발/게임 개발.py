import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

in_degree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
costs = [0 for _ in range(N+1)]
for v1 in range(1,N+1):
    tmp = list(map(int,input().split()))
    costs[v1] = tmp[0]
    for v2 in tmp[1:-1]:
        in_degree[v1] += 1
        graph[v2].append(v1)

dist = [0 for _ in range(N+1)]
queue = deque()
for v1 in range(1,N+1):
    if in_degree[v1] == 0:
        queue.append(v1)
        dist[v1] = costs[v1]

while queue:
    v1 = queue.popleft()
    
    for v2 in graph[v1]:
        in_degree[v2] -= 1
        if in_degree[v2] == 0:
            queue.append(v2)
        dist[v2] = max(dist[v1] + costs[v2], dist[v2])

for d in dist[1:]:
    print(d)