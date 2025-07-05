import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]


degree = [0 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(int(input())):
    x,y,k = map(int,input().split())
    graph[y].append([x,k])
    degree[x] += 1

res = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    if not degree[i]:
        res[i][i] = 1

visited = [0 for _ in range(N+1)]
for _ in range(N):
    v1 = 0
    for i in range(1,N+1):
        if degree[i] == 0 and not visited[i]:
            v1 = i
            visited[i] = 1
            break
    for v2,cost in graph[v1]:
        for i in range(1,N+1):
            res[v2][i] += res[v1][i]*cost
        degree[v2]-=1

for i in range(1,N+1):
    if res[N][i] > 0:
        print(i,res[N][i])