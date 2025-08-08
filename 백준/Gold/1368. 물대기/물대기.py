import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())

hq = [(int(input()),i) for i in range(N)]
cost = [list(map(int,input().split())) for _ in range(N)]
visited = [0 for _ in range(N+1)]
min_cost = 0
heapq.heapify(hq)
while hq:
    curr_cost,v1 = heapq.heappop(hq)
    if visited[v1]:
        continue
    min_cost += curr_cost
    visited[v1] = 1
    for v2 in range(N):
        if v1 == v2:
            continue
        heapq.heappush(hq,(cost[v1][v2], v2))
print(min_cost)