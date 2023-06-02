import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
virus = []
for _ in range(M):
    node,num = map(int,input().split())
    graph[node].append(num)
    graph[num].append(node)

visited = [False for _ in range(N+1)]
def BFS(graph, start, visited):
    queue = deque([])
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                virus.append(i)
                queue.append(i)
                BFS(graph,i,visited)
BFS(graph, 1, visited)
print(len(virus))
