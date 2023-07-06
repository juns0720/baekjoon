import sys
from collections import deque
input = sys.stdin.readline

N,M,V = map(int,input().split())
graph = [[] for i in range(N+1)]
visited_DFS, visited_BFS = [False] * (N+1), [False] * (N+1)
res1, res2 = '', ''
queue = deque([])
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def DFS(node,res1):
    visited_DFS[node] = True
    res1 += str(node)+' '

    for i in sorted(graph[node]):
        if visited_DFS[i] != True:
            res1 = DFS(i,res1)

    return res1

def BFS(node,res2):
    visited_BFS[node] = True
    res2 +=str(node)+' '

    for i in sorted(graph[node]):
        if visited_BFS[i] != True:
            if i not in queue:
                queue.append(i)
    if len(queue) != 0:
        res2 = BFS(queue.popleft(),res2) 
    return res2

print(DFS(V,res1))
print(BFS(V,res2))
