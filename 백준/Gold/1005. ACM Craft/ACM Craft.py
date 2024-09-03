import sys
from collections import deque
input = sys.stdin.readline

for tc in range(int(input())):
    N,K = map(int,input().split())
    costs = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(N+1)]
    degree = [0 for _ in range(N+1)]
    sec = 0
    for i in range(K):
        v1,v2 = map(int,input().split())
        degree[v2]+=1
        graph[v1].append(v2)
    W = int(input())
    res = [0 for _ in range(N+1)]
    queue = deque()
    for v in range(1,N+1):
        if degree[v] == 0:
            queue.append(v)
            res[v] = costs[v]



    while queue:
        v1 = queue.popleft()
        tmp = 0
        if v1 == W:
            print(res[W]) 
            break
        for v2 in graph[v1]:
            degree[v2]-=1
            if degree[v2] == 0:
                queue.append(v2)
            res[v2] = max(res[v2], res[v1]+costs[v2])
