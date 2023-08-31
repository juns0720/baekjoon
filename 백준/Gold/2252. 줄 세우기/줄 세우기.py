import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
res = []
graph = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
queue = deque([])
def check():
    for i in range(1,len(degree)):
        if degree[i] == 0:
            queue.append(i)
            degree[i] = -1
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b]+=1
check()
while queue:
    node = queue.popleft()
    print(node,end=' ')
    for v in graph[node]:
        degree[v]-=1
    check()