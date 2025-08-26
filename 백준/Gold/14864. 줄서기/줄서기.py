import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())

degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
check = [i for i in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
    degree[a] += 1

    check[a-1] += 1
    check[b-1] -= 1

if len(set(check)) < n:
    print(-1)
    exit()

hq = []
for i in range(1,n+1):
    if degree[i] == 0:
        heapq.heappush(hq,i)

res = [0 for _ in range(n+1)]

num = 1
while hq:
    v1 = heapq.heappop(hq)
    res[v1] = num
    num += 1
    for v2 in graph[v1]:
        if not degree[v2]:
            continue
        degree[v2] -= 1
        if degree[v2] == 0:
            heapq.heappush(hq,v2)

print(*res[1:])
