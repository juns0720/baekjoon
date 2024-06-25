import sys
from collections import deque
input = sys.stdin.readline

n = int(input())


graph = [[] for _ in range(n+1)]

queue = deque([])
visited = [0 for _ in range(n+1)]

def bfs():
    max_dist = -1
    while queue:
        v1, dist= queue.popleft()
        max_dist = max(dist, max_dist)
        for v2,cost in graph[v1]:
            if not visited[v2]:
                visited[v2] = 1
                queue.append((v2, dist+cost))
    return max_dist


for i in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
queue.append((1,0))
visited[1] = 1
print(bfs())