import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N, M, K = map(int,input().split())


dic = dict()
for i in range(M):
    v1,v2,c = map(int,input().split())
    if (v1,v2) in dic:
        dic[(v1,v2)] = min(dic[(v1,v2)], c)
    else:
        dic[(v1,v2)] = c

#그래프 생성
graph = [[] for _ in range(N+1)]
for v,c in dic.items():
    v1,v2 = v
    graph[v2].append((v1,c))

#목적지
dest = dict()
for v in list(map(int,input().split())):
    dest[v] = 1

def dijkstra():
    dist = [INF for _ in range(N+1)]    
    hq = []

    for v in dest.keys():
        heapq.heappush(hq,(0,v))
        dist[v] = 0

    while hq:
        cost, v1 = heapq.heappop(hq)
        if dist[v1] < cost:
            continue

        for v2, cur_cost in graph[v1]:
            if dist[v2] < cost + cur_cost:
                continue

            dist[v2] = cost + cur_cost
            heapq.heappush(hq,(dist[v2],v2))

    min_dist = 0
    min_v = 0
    for v in range(1,N+1):
        if dist[v] == INF or v in dest or dist[v] < min_dist:
            continue

        if dist[v] == min_dist:
            min_v = min(v, min_v)
        else:
            min_dist = dist[v]
            min_v = v
    print(min_v)
    print(min_dist)
        
dijkstra()