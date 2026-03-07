import sys
from collections import deque
import heapq
input = sys.stdin.readline


for tc in range(1, int(input()) + 1):


    k,m,p = map(int,input().split())

    degree = [0 for _ in range(m+1)]
    graph = [[] for _ in range(m+1)]

    for i in range(p):
        a,b = map(int,input().split())
        degree[b] += 1
        graph[a].append((b))
        graph[b].append((a))


    strahler = [[0,[]] for _ in range(m+1)]
    queue = deque()
    res = [0 for _ in range(m+1)]
    for i in range(1,m+1):
        if degree[i] == 0:
            queue.append((i,1))
            strahler[i][0] = 1
            heapq.heappush(strahler[i][1], -1)


    
    while queue:
        v1, depth = queue.popleft()

        strahler[v1][0] = -heapq.heappop(strahler[v1][1])
        if len(strahler[v1][1]) > 0 and strahler[v1][0] == -heapq.heappop(strahler[v1][1]):
            strahler[v1][0] += 1

        for v2 in graph[v1]:

            if degree[v2] > 0:
                heapq.heappush(strahler[v2][1], -strahler[v1][0])
                degree[v2] -= 1

                if degree[v2] == 0:
                    queue.append((v2,depth+1))
        
    print(k,strahler[m][0])
