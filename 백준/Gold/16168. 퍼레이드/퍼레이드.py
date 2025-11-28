import sys
from collections import deque
input = sys.stdin.readline

V,E = map(int,input().split())

graph = [[] for _ in range(V+1)]

for i in range(E):
    a,b = map(int,input().split() )
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited = [0 for _ in range(V+1)]
visited[1] = 1

tv = 1
while queue:
    v1 = queue.popleft()
    
    for v2 in graph[v1]:
        if visited[v2]:
            continue

        visited[v2] = 1
        queue.append(v2)
        tv += 1

if tv != V:
    print("NO")
    exit()
    
cnt = 0
for i in range(1,V+1):
    if len(graph[i]) % 2 == 1:
        cnt += 1

if cnt in [0,2]:
    print("YES")
else:
    print("NO")