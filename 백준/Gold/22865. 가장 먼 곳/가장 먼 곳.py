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
def dijkstra():

    while hq:
        cost,v1 = heapq.heappop(hq)
        if dist[v1] < cost:
            continue
        for v2,curr_cost in graph[v1]:
            if dist[v2] < cost + curr_cost:
                continue
            dist[v2] = cost+curr_cost
            heapq.heappush(hq,(dist[v2],v2))



dist = [INF for _ in range(N+1)]
hq = []
for i in range(3):
    heapq.heappush(hq,(0,target[i]))
    dist[target[i]] = 0
dijkstra()

max_dist = 0
v1 = 0
for v2,curr_dist in enumerate(dist[1:]):
    if v2+1 in target:
        continue
    if curr_dist > max_dist:
        max_dist = curr_dist
        v1 = v2+1
print(v1)