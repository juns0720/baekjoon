import sys
import math
import heapq
input = sys.stdin.readline
INF = math.inf
'''
N개의 노드, M개의 간선, K위치에서 탐색
다익스트라, 양방향 그래프

1. 다익스트라로 해당 친구들 위치에서 거리 탐색해서
2. 전체 거리 배열에 전부 더함
3. 전체 거리 배열 정렬해서 출력
'''

def dijkstra(start_node):
    hq = []
    heapq.heappush(hq, (start_node, 0))
    dist = [INF for _ in range(N+1)]
    dist[start_node] = 0

    while hq:
        v1, total_dist = heapq.heappop(hq)
        if dist[v1] < total_dist:
            continue

        for v2 , cur_dist in graph[v1]:
            if total_dist+cur_dist < dist[v2]:
                dist[v2] = total_dist+cur_dist
                heapq.heappush(hq,(v2, total_dist+cur_dist))
    for i in range(1, N+1):
        res_dist[i][1]+=dist[i]
for _ in range(int(input())):
    N,M = map(int,input().split())
    res_dist = [[i,0] for i in range(N+1)]
    res_dist[0][1] = INF
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        v1,v2,cost = map(int,input().split())
        graph[v1].append((v2,cost))
        graph[v2].append((v1,cost))
    K = int(input())
    friends = list(map(int,input().split()))
    for friend in friends:
        dijkstra(friend)
    res_dist.sort(key = lambda x: (x[1], x[0]))
    print(res_dist[0][0])
