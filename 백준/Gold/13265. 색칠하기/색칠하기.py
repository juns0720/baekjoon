import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while queue:
        v1= queue.popleft()
        for v2 in graph[v1]:
            if color[v2] == color[v1]:
                return 0
            if visited[v2]:
                continue
            color[v2] = (color[v1]+1)%2
            visited[v2] = 1
            queue.append(v2)
    return 1



for tc in range(int(input())):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    color = [-1 for _ in range(n+1)]
    for _ in range(m):
        v1,v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    for v1 in range(1,n+1):
        if visited[v1]:
            continue
        queue = deque()
        queue.append(v1)
        visited[v1] = 0
        color[v1] = 0
        if not bfs():
            print("impossible")
            break
    else:
        print('possible')
