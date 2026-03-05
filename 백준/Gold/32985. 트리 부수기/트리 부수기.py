import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]

for i in range(N-1):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def bfs():

    while queue:
        v1, depth = queue.popleft()
        res[v1] -= 1*depth

        for v2 in graph[v1]:
            if visited[v2]:
                continue

            visited[v2] = 1
            queue.append((v2,depth+1))
            

queue = deque([(0,0)])
res = [N-1 for _ in range(N)]

visited = [0 for _ in range(N)]
visited[0] = 1

bfs()

for i in list(reversed(res[1:])):
    print(1 if i % 2 == 1 else 0, end = '')