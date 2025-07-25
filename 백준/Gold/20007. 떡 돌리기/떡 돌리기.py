import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m,x,y = map(int,input().split())
dist = [INF for _ in range(n)]
dist[y] = 0
hq = [(0,y)]
heapq.heapify(hq)
graph = [[] for _ in range(n)]

def dijkstra():
    while hq:
        cur_cost,v1 = heapq.heappop(hq)
        if dist[v1] < cur_cost:
            continue
        for v2,cost in graph[v1]:
            if cur_cost + cost < dist[v2]:
                dist[v2] = cur_cost + cost
                heapq.heappush(hq,(cur_cost + cost, v2))


for _ in  range(m):
    v1,v2,cost = map(int,input().split())
    graph[v1].append((v2,cost))
    graph[v2].append((v1,cost))
dijkstra()
dist.sort()
total = 0
day = 0
for d in dist:
    if d*2 > x:
        print(-1)
        exit()
    if total + d*2 > x:
        day += 1
        total = d*2
    else:
        total += d*2
if total:
    day += 1
print(day)