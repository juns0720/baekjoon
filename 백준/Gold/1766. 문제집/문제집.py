import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())

degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

hq = []
for i in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    degree[v2]+=1

for gph in graph:
    gph.sort()

for i in range(n):
    for v1 in range(1,n+1):
        if degree[v1] == 0 and not visited[v1]:
            visited[v1] = 1
            heapq.heappush(hq,v1)
            for v2 in graph[v1]:
                degree[v2]-=1
            break
    while hq:
        print(heapq.heappop(hq), end = ' ')