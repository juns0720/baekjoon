import sys
import math
import heapq
input = sys.stdin.readline

n = int(input())
e = int(input())

INF = math.inf
graph = [[] for _ in range(n+1)]

for i in range(e):
    v1,v2,cost = map(int,input().split())
    graph[v1].append((v2,cost))

s,e = map(int,input().split())
parent = [-1 for _ in range(n+1)]
dist = [INF for _ in range(n+1)]
dist[s] = 0

def dijkstra(start,end):
    hq = []
    heapq.heappush(hq, (0,start))

    while hq:
        cur_dist, v1 = heapq.heappop(hq)
        if dist[v1] < cur_dist:
            continue

        for v2,cost in graph[v1]:
            if dist[v2] > cur_dist+cost:
                dist[v2] = cur_dist+cost
                parent[v2] = v1
                heapq.heappush(hq,(dist[v2], v2))

dijkstra(s,e)
path = []
now_node = e
path.append(now_node)

while now_node != s:
    now_node = parent[now_node]
    path.append(now_node)

print(dist[e])
print(len(path))
print(*reversed(path))