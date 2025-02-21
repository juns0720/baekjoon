import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize
def dijkstra():
    costs = [INF for _ in range(m)]
    costs[0] = 0
    hq = []
    heapq.heappush(hq,(0,0))
    node = [i for i in range(m)]
    while hq:
        cur_cost,v1 = heapq.heappop(hq)
        if cur_cost > costs[v1]:
            continue

        for v2,cost in graph[v1]:
            if cur_cost + cost < costs[v2]:
                heapq.heappush(hq,(cur_cost + cost,v2))
                costs[v2] = cur_cost + cost
                node[v2] = v1
    if costs[m-1] == INF:
        print(f'Case #{tc}: -1')
    else:
        v = m-1
        seq = [v]
        while True:
            seq.append(node[v])
            v = node[v]
            if v == 0:
                break
        print(f'Case #{tc}: ', end = '')
        print(*reversed(seq))
for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    graph = [[] for _ in range(m+1)]
    for i in range(n):
        v1,v2,cost = map(int,input().split())
        graph[v1].append((v2,cost))
        graph[v2].append((v1,cost))
    dijkstra()