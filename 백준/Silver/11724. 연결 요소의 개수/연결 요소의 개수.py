import sys
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
vertex = [i for i in range(1,N+1)]
visited=[False for _ in range(N+1)]
cnt = 0
for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def DFS(node):
    visited[node] = True
    for i in graph[node]:
        if visited[i] != True:
            DFS(i)
for i in vertex:
    if visited[i] == False:
        DFS(i)
        cnt+=1
print(cnt)
