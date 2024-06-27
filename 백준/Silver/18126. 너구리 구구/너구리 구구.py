import sys
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = 0

for i in range(n-1):
    v1,v2,cost = map(int,input().split())
    #v1 -> v2 일 때의 cost
    graph[v1].append((v2, cost))
        #v2 -> v1 일 때의 cost
    graph[v2].append((v1, cost))


def dfs(current_node, current_dist):
    global result
    visited[current_node] = True
    result = max(result, current_dist)
    for next_node, dist in graph[current_node]:
        if not visited[next_node]:
            dfs(next_node, current_dist + dist)

    
dfs(1,0)
print(result)

