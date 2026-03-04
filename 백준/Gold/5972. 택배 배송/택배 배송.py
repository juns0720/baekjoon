import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1,v2,c = map(int,input().split())
    graph[v1].append((v2,c))
    graph[v2].append((v1,c))

dist = [INF for _ in range(N+1)]
dist[1] = 0

hq = []
heapq.heappush(hq, (0,1))

while hq:
    cur_dist, v1 = heapq.heappop(hq)

    if dist[v1] < cur_dist:
        continue
    
    for v2,cost in graph[v1]:

        if cost + dist[v1] < dist[v2]:
            dist[v2] = cost + dist[v1]
            heapq.heappush(hq,(dist[v2], v2))

print(dist[N])