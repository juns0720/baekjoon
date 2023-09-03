import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
board = [[0 for _ in range(N)] for _ in range(N)]
queue = deque([])
for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            graph[i].append(j)
def BFS(v1):
    while queue:
        node = queue.popleft()
        for v2 in graph[node]:
            if not visited[v2]:
                board[v1][v2] = 1
                queue.append(v2)
                visited[v2] = 1

queue = deque([])
for i in range(N):
    visited = [0 for _ in range(N+1)]
    queue.append(i)
    BFS(i)
for i in board:
    for j in i:
        print(j,end=' ')
    print()