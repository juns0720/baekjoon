import sys
import math
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
    exit()

graph = [[] for _ in range(N+1)]

ratio = [[[] for _ in range(N+1)] for _ in range(N+1)]
for _ in range(N-1):
    v1, v2, v1_ratio, v2_ratio = map(int,input().split())
    
    graph[v1].append(v2)
    ratio[v1][v2] = [v1_ratio,v2_ratio]
    graph[v2].append(v1)
    ratio[v2][v1] = [v2_ratio,v1_ratio]

res = [[0,0] for _ in range(N)]
res[0] = [1,1]
visited = [0 for _ in range(N)]


def dfs(v1):
    for (v2) in graph[v1]:
        if not visited[v2]:
            for i in range(2):
                res[v2][i] = res[v1][i]*ratio[v1][v2][i]
            visited[v2] = 1
            dfs(v2)
visited[0] = 1
dfs(0)

lcm = 1
for i in res:
    gcd = math.gcd(i[0],i[1])
    i[0],i[1] = i[0]//gcd, i[1]//gcd
    
for i in range(1,N):
    lcm = math.lcm(lcm,res[i][0])

for i in res:

    print(i[1]*(lcm//i[0]), end =' ')
