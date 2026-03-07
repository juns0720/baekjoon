import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    degree[b] += 1
    graph[a].append((b))
    graph[b].append((a))

queue = deque()
res = [0 for _ in range(n+1)]
for i in range(1,n+1):
    if degree[i] == 0:
        queue.append((i,1))


while queue:
    v1, depth = queue.popleft()
    res[v1] = depth
    for v2 in graph[v1]:

        if degree[v2] > 0:
            degree[v2] -= 1

            if degree[v2] == 0:
                queue.append((v2,depth+1))
    
print(*res[1:])