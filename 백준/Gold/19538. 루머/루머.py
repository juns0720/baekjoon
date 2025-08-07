import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
res = [[0,-1] for _ in range(N+1)]
mid = [0 for _ in range(N+1)]

for v1 in range(1,N+1):
    tmp = list(map(int,input().split()))[:-1]
    l = len(tmp)
    if l % 2 == 0 and l != 0:
        l = (l//2)-1 
    else:
        l = l//2
    mid[v1] = l
    for v2 in tmp:
        graph[v1].append(v2)

M = int(input())
queue = deque()
for v1 in list(map(int,input().split())):
    queue.append((v1,1))
    res[v1][0],res[v1][1] = [mid[v1]+1,0]

def bfs():
    cost = 0
    while queue:
        v1,cost = queue.popleft()

        for v2 in graph[v1]:
            res[v2][0] += 1

            if res[v2][0] > mid[v2] and res[v2][1] == -1:
                res[v2][1] = cost
                queue.append((v2,cost+1))

bfs()
for i in range(1,N+1):
    print(res[i][1],end = ' ')
