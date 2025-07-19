import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
dist = [-1 for _ in range(n+1)]

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))
    reverse_graph[v2].append((v1, cost))
    indegree[v2] += 1

s, e = map(int, input().split())
dist[s] = 0
queue = deque([s])

while queue:
    v1 = queue.popleft()
    for v2, cost in graph[v1]:
        if dist[v2] < dist[v1] + cost:
            dist[v2] = dist[v1] + cost
        indegree[v2] -= 1
        if indegree[v2] == 0:
            queue.append(v2)

res = 0
visited = [0 for _ in range(n+1)]
queue = deque([e])
visited[e] = True

while queue:
    v1 = queue.popleft()
    for v2, cost in reverse_graph[v1]:
        if dist[v1] == dist[v2] + cost:
            res += 1
            if visited[v2]:
                continue
            visited[v2] = 1
            queue.append(v2)

print(dist[e])
print(res)
