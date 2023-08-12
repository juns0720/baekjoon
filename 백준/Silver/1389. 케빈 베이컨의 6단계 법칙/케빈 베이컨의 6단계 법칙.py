import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
queue = deque([])
user = dict()
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS():
    bacon = [0 for _ in range(N+1)]
    while queue:
        node = queue.popleft()
        for v in graph[node]:
            if not visited[v]:
                bacon[v] = bacon[node]+1
                queue.append(v)
                visited[v] = 1 
    return sum(bacon)

for i in range(1,N+1):
    visited = [0 for _ in range(N+1)]
    queue.append(i)
    visited[i] = 1
    user[i] = (BFS())
print(min(user, key = lambda x : user[x]))
