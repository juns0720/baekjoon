import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline

N = int(input())

color = [0]+list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
visited = [0 for i in range(N+1)]
res = 0

for i in range(N-1):
    a,b = map(int,input().split())
    graph[b].append(a)
    graph[a].append(b)
            
def dfs(v1,c):
    global res
    for v2 in graph[v1]:
        if not visited[v2]:
            visited[v2] = 1
            if color[v2] != c:
                res+=1
            dfs(v2,color[v2])
visited[1] = 1
if color[1]:
    res+=1
dfs(1,color[1])
print(res)