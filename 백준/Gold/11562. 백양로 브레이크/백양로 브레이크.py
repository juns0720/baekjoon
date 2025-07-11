import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
INF = sys.maxsize

graph = [[] for _ in range(n+1)]
board = [[INF for _ in range(n+1)] for _ in range(n+1)]


for _ in range(m):
    v1,v2,f = map(int,input().split())
    graph[v1].append((v2,0))
    if f == 0:
        graph[v2].append((v1,1))
    else:
        graph[v2].append((v1,0))



def bfs(start):
    while queue:
        v1 = queue.popleft()
        for v2,cost in graph[v1]:
            if board[start][v2] > board[start][v1] + cost:
                board[start][v2] = board[start][v1] + cost
                queue.append(v2)


for i in range(1,n+1):
    queue = deque([i])
    board[i][i] = 0
    bfs(i)

for _ in range(int(input())):
    s,e = map(int,input().split())
    print(board[s][e])