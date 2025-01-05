import sys
from collections import deque
input = sys.stdin.readline


def bfs(key):
    while True:
        v1 = queue.popleft()
        for v2 in graph[v1]:
            if v2 == key:
                return 1
            if not visited[v2]:
                queue.append(v2)
                visited[v2] = 1
    return 0

tc = 1
while True:

    n = int(input())
    if n == 0:
        break

    graph = [[] for _ in range(n+1)]
    dic = dict()
    node_idx = 1

    for i in range(n):
        nodes = list(input().split())
        for node in nodes:
            if node not in dic:
                dic[node] = node_idx
                node_idx+=1
        graph[dic[nodes[0]]].append(dic[nodes[1]])

    visited = [0 for _ in range(n+1)]
    queue = deque()
    res = 0
    for v1 in range(1,n+1):
        if not visited[v1]:
            queue.append(v1)
            visited[v1] = 1
            res +=bfs(v1)
    print(f"{tc} {res}")
    tc+=1

