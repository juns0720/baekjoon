import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
INF = sys.maxsize
graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dijkstra(c1,c2):
    dist = [INF for _ in range(n+1)]
    dist[c1] = 0
    dist[c2] = 0
    hq = []
    heapq.heappush(hq,(0,c1))
    heapq.heappush(hq,(0,c2))

    while hq:
        curr_dist,v1 =  heapq.heappop(hq)
        if dist[v1] < curr_dist:
            continue

        for v2 in graph[v1]:
            if dist[v2] < curr_dist + 1:
                continue
            dist[v2] = curr_dist + 1
            heapq.heappush(hq,(dist[v2],v2))
    res = 0
    for d in dist[1:]:
        res += d*2
    return res

min_res = INF
c1,c2 = 0,0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        res = dijkstra(i,j)
        if res < min_res:
            c1,c2 = i,j
            min_res = res

print(c1,c2,min_res)