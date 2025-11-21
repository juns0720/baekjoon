import sys
from collections import deque
import heapq
input = sys.stdin.readline
'''
한별의 이동 경로 -> 학교
1. 연결된 간선이 가장 많은 노드
2. 가장 번호가 큰 노드
3. 총 노드가 가장 적은 경로를 통해 등교(이전 경로를 계속 기억한다.)


토카 경로
1. 한별이 지나치는 노드 중 토카네 집에서 가장 빨리 도착할 수 있는 노드
2. 번호가 가장 작은 노드

설계
1. 한별의 집 -> 학교 이동 경로를 탐색한다. BFS?
2. 토카의 집에서 BFS를 진행하여 한별이 지나친 노드 중 가장 거리가 짧은 노드를 탐색한다.
'''
dic = dict()
N,M = map(int,input().split())
#토카, 한별, 학교의 위치    
A,B,C = map(int,input().split())
INF = sys.maxsize
graph = [[] for _ in range(N+1)]
edge = [0 for _ in range(N+1)]
for i in range(M):
    v1, v2, c = map(int,input().split())
    edge[v1] += 1
    edge[v2] += 1
    v1,v2 = min(v1,v2), max(v1,v2)
    if (v1,v2) in dic:
        dic[(v1,v2)] = min(dic[(v1,v2)], c)
    else:
        dic[(v1,v2)] = c

for p,c in dic.items():
    v1,v2 = p[0], p[1]
    graph[v1].append((v2,c,edge[v2]))
    graph[v2].append((v1,c,edge[v1]))


for i in range(1,N+1):
    graph[i].sort(key = lambda x: (-x[2], -x[0]))


pos = [0 for _ in range(N+1)]

def bfs_htos():
    queue = deque([])
    visited = [0 for _ in range(N+1)]
    queue.append(B)
    visited[B] = 1

    while queue:
        v1 = queue.popleft()

        if v1 == C:
            i = C
            path = [C]
            while i != B:
                path.append(pos[i])
                i = pos[i]
            return path
    
        for v2,c,e in graph[v1]:
            if visited[v2]:
                continue
            queue.append(v2)
            visited[v2] = 1
            pos[v2] = v1


def dijkstra_ttoh():
    dist = [INF for _ in range(N+1)]
    dist[A] = 0
    hq = []
    heapq.heappush(hq,(0,A))

    while hq:
        cur_dist, v1 = heapq.heappop(hq)

        if dist[v1] < cur_dist:
            continue

        for v2, cost, deg in graph[v1]:
            if dist[v2] > dist[v1] + cost:
                dist[v2] = dist[v1] + cost
                heapq.heappush(hq, (dist[v2], v2))

    
    return dist

h_path = set(bfs_htos())
res = []
dist = dijkstra_ttoh()
for v1 in h_path:
    res.append((v1,dist[v1]))

res.sort(key = lambda x: (x[1],x[0]))
print(res[0][0])