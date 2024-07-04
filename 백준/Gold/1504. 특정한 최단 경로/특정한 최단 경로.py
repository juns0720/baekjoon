import sys
import math
import heapq
input = sys.stdin.readline

n,e = map(int,input().split())
INF = math.inf
graph = [[] for _ in range(n+1)]


for i in range(e):
    v1,v2,cost = map(int,input().split())
    graph[v1].append((v2,cost))
    graph[v2].append((v1,cost))

ey,ex = map(int,input().split())

#시작 -> ey + ey -> ex + ex -> 끝
# ''  -> ex
def dijkstra(start,end):
    dist = [INF for _ in range(n+1)]
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0,start))

    while hq:
        cur_dist, v1 = heapq.heappop(hq)
        if dist[v1] < cur_dist:
            if v1 == end:
                break
            continue


        for v2,cost in graph[v1]:
            if dist[v2] > cur_dist+cost:
                dist[v2] = cur_dist+cost
                heapq.heappush(hq,(dist[v2], v2))
            
    return dist[end]

dist1 = dijkstra(1,ey) + dijkstra(ey,ex) + dijkstra(ex,n)
dist2 = dijkstra(1,ex) + dijkstra(ex,ey) + dijkstra(ey,n)
res = min(dist1, dist2)

if res == INF:
    print(-1)
else:
    print(res)
