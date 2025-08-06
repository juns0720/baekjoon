import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
target = list(map(int,input().split()))
M = int(input())

graph = [[] for _ in range(N+1)]
for i in range(M):
    v1,v2,cost = map(int,input().split())
    graph[v1].append((v2,cost))
    graph[v2].append((v1,cost))

res = []
def dijkstra(s,i):

    hq = []
    heapq.heappush(hq,(0,s))
    dist[i][s] = 0

    while hq:
        cost,v1 = heapq.heappop(hq)
        if dist[i][v1] < cost:
            continue
        for v2,curr_cost in graph[v1]:
            if dist[i][v2] < cost + curr_cost:
                continue
            dist[i][v2] = cost+curr_cost
            heapq.heappush(hq,(dist[i][v2],v2))



dist = [[INF for _ in range(N+1)] for _ in range(3)]
for i in range(3):
    dijkstra(target[i],i)

max_dist = 0
v1 = 0
for v2 in range(1,N+1):
    if v2 in target:
        continue
    curr_dist = INF

    for j in range(3):
        curr_dist = min(dist[j][v2], curr_dist)

    if max_dist < curr_dist:
        max_dist = curr_dist
        v1 = v2

print(v1)