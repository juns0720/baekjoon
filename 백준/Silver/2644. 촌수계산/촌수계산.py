import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
start,end = map(int,input().split())
M = int(input())
cnt = -1
graph = [[] for i in range(N+1)]
visited = [False]*(N+1)
queue = deque([])

for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
search = []

def DFS(node,end,cnt):
    visited[node] = True
    cnt+=1
    if node == end:
        search.append(cnt)
        return
    for i in sorted(graph[node]):
        if visited[i] != True:
            DFS(i,end,cnt)
    return
DFS(start,end,cnt)
if len(search) == 0:
    print(-1)
else:
    print(min(search))
    
