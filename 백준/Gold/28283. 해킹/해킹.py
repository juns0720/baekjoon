import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize
N,M,X,Y = map(int,input().split())
cost = [0] + list(map(int,input().split()))


graph = [[] for _ in range(N+1)]
for i in range(M):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dist = [INF for _ in range(N+1)]

hq = []
for v1 in list(map(int,input().split())):
    heapq.heappush(hq, (0,v1))
    dist[v1] = 0

def dijkstra():

    while hq:
        cur_dist, v1 = heapq.heappop(hq)

        if dist[v1] < cur_dist:
            continue

        for v2 in graph[v1]:
            if dist[v2] < cur_dist + 1:
                continue

            dist[v2] = cur_dist+1
            heapq.heappush(hq,(dist[v2], v2))
dijkstra()
res = []

for i in range(1,N+1):
    if dist[i] == INF and cost[i] != 0:
        print(-1)
        exit()

    res.append(dist[i]*cost[i]) 
res.sort(reverse = True)

print(sum(res[:X]))