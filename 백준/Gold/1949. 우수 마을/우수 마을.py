import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
costs = [0] + list(map(int,input().split()))
dp = [[0,0] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(v1):

    tmp = [0,costs[v1]]
    for v2 in graph[v1]:
        if visited[v2]:
            continue

        visited[v2] = 1
        child = dfs(v2)

        tmp[0] += max(child[0], child[1])
        tmp[1] += child[0]

    return tmp

visited = [0 for _ in range(N+1)]
visited[1] = 1
print(max(dfs(1)))