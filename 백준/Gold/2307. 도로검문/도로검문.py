import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
edge = deque([])
for i in range(m):
    a,b,t = map(int,input().split())
    edge.append((a,b,t))
    graph[a].append((b,t))
    graph[b].append((a,t))

def dijkstra(a):
    dist = [INF for _ in range(n+1)]
    dist[1] = 0
    hq = []
    heapq.heappush(hq,(0,1))
    while hq:
        cost, v1 = heapq.heappop(hq)
        if dist[v1] < cost:
            continue
        for v2,crnt_cost in graph[v1]:
            #검문 하는 간선이라면
            if v2 == a:
                continue
            if crnt_cost + cost < dist[v2]:
                dist[v2] = crnt_cost + cost
                heapq.heappush(hq,(crnt_cost + cost,v2))
    return dist[n]

dist = dijkstra(-1)
res = 0
for i in range(2,n):
    #검문 할 간선
    crnt_dist = dijkstra(i)
    if crnt_dist == INF:
        print(-1)
        exit()
    res = max(res,abs(dist-crnt_dist))

print(res)