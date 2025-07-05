import sys
import heapq
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

V,E = map(int,input().split())
hq = []
parent = [i for i in range(V+1)]

def find(v):
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]


def union(v1,v2):
    v1 = find(v1)
    v2 = find(v2)
    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2

weight = 0
for _ in range(E):
    v1, v2, cost = map(int,input().split())
    heapq.heappush(hq, (cost,v1,v2))

while hq:
    cost, v1, v2 = heapq.heappop(hq)
    if find(v1) != find(v2):
        weight+=cost
        union(v1,v2)
print(weight)