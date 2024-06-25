import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
res_dfs = []
res_bfs = []
# 양방향 그래프이므로 v1 -> v2, v2 -> v1 연결
for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 다른 정점을 방문할 때 정점 번호가 작은 것을 먼저 방문하므로 오름차순으로 정렬
for v1 in range(1,n+1):
    graph[v1].sort()


def dfs(v1):
    visited[v1] = 1
    res_dfs.append(v1)

    for v2 in graph[v1]:
        if not visited[v2]:
            dfs(v2)


def bfs(start_node):
    queue = deque([])
    visited = [0 for _ in range(n+1)]

    visited[start_node] = 1
    res_bfs.append(start_node)
    queue.append(start_node)


    while queue:
        v1 = queue.popleft()
        
        for v2 in graph[v1]:
            if not visited[v2]:
                visited[v2] = 1
                res_bfs.append(v2)
                queue.append(v2)


visited = [0 for _ in range(n+1)]
dfs(v)

bfs(v)

# 언패킹 -> 리스트 풀어줌
print(*res_dfs)
print(*res_bfs)