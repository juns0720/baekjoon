import sys
import heapq
input = sys.stdin.readline

'''
1. 각 분리된 마을 안에 집들이 서로 연결되어야 한다.
2. 분리된 두 마을사이에 있는 길들은 제거할 수 있다.
3. 분리된 마을 안에서도 길을 더 제거할 수 있다.
 = 최소 스패닝 트리 구한 후 최대 길이 제거
'''
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1,v2):
    v1 = find(v1)
    v2 = find(v2)
    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2

N,M = map(int,input().split())
hq = []
max_dist = -1
res = 0
visited = [0 for _ in range(N+1)]
parent = [i for i in range(N+1)]
for i in range(M):
    v1,v2,dist = map(int,input().split())
    heapq.heappush(hq,(dist,v1,v2))

while hq:
    dist,v1,v2 = heapq.heappop(hq)
    if find(v1) != find(v2):
        union(v1,v2)
        res+=dist
        max_dist = max(max_dist,dist)
        visited[v1],visited[v2] = 1,1
print(res-max_dist)
