import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def total_friends(v1,v2,v3):
    return (len(graph[v1]) + len(graph[v2]) + len(graph[v3])) - 6

res = -1
for s in range(1,N+1):
    for m in graph[s]:
        for e in graph[m]:
            if s in graph[e]:
                if res == -1:
                    res = total_friends(s,m,e)
                else:
                    res = min(res, total_friends(s,m,e))
print(res)