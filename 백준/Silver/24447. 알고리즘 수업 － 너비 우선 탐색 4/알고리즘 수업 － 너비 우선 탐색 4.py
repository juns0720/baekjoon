import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in graph:
    i.sort()
queue = deque([])
visited =[0 for _ in range(n+1)]
queue.append((r,0))
visited[r] = 1
res = 0
d = [-1 for _ in range(n+1)]
t = [0 for _ in range(n+1)]
def bfs():
    cnt = 0
    while queue:
        v1, depth = queue.popleft()
        cnt += 1
        d[v1] = depth
        t[v1] = cnt
        for v2 in graph[v1]:
            if not visited[v2]:
                queue.append((v2,depth+1))
                visited[v2] = 1
bfs()
for i in range(1,n+1):
    res += t[i]*d[i]
print(res)