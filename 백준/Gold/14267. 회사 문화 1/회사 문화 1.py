import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for i in range(1,n):
    graph[arr[i]].append(i+1)
cnt = [0 for _ in range(n+1)]

for _ in range(m):
    i,w = map(int,input().split())
    cnt[i]+=w
queue = deque([(1,0)])
res = [0 for _ in range(n+1)]
while queue:
    v1,cost = queue.popleft()
    res[v1] = cost
    for v2 in graph[v1]:
        queue.append((v2,cost+cnt[v2]))

print(*res[1:])