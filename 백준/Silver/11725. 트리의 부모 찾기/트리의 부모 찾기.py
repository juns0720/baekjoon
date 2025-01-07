import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(n-1):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(v1):
    for v2 in graph[v1]:
        if not visited[v2]:
            visited[v2] = v1
            dfs(v2)

for i in range(1,n+1):
    if not visited[i]:
        visited[i] = i
        dfs(i)

for v in visited[2:]:
    print(v)