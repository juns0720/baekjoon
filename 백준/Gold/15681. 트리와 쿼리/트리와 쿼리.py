import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


N,R,Q = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
visited = [0 for _ in range(N+1)]
path = []

def DFS(v1):
    visited[v1]+=1
    for v2 in graph[v1]:
        if not visited[v2]:
            DFS(v2)
            visited[v1]+=visited[v2]

DFS(R)
for i in range(Q):
    print(visited[int(input())])
