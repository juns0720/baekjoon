import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]

for i in range(N-1):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(v1, depth):
    res[v1] -= 1*depth

    for v2 in graph[v1]:
        if visited[v2]:
            continue

        visited[v2] = 1
        dfs(v2,depth + 1)

res = [N-1 for _ in range(N)]
visited = [0 for _ in range(N)]
visited[0] = 1
dfs(0,0)

for i in list(reversed(res[1:])):
    print(1 if i % 2 == 1 else 0, end = '')