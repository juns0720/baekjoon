import sys
import heapq
from math import gcd
input = sys.stdin.readline

N = int(input())
seq = list(map(int,input().split()))

indegree = [0 for _ in range(N+1)]

graph = [[] for _ in range(N+1)]
for i in range(N):
    for j in range(i-1,-1,-1):
        if gcd(seq[i], seq[j]) == 1:
            continue

        indegree[i] += 1
        graph[j].append(i)

hq = []
for i in range(N):
    if not indegree[i]:
        heapq.heappush(hq, (seq[i],i))

res = []
while hq:
    n1, v1 = heapq.heappop(hq)
    res.append(n1)
    for v2 in graph[v1]:
        indegree[v2] -= 1
        if not indegree[v2]:
            heapq.heappush(hq,(seq[v2],v2))

print(*res)