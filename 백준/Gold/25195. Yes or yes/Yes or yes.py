import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)


S = int(input())

fan = [0 for _ in range(N+1)]

for f in list(map(int,input().split())):
    fan[f] = 1

if fan[1] == 1:
    print("Yes")
    exit()

visited = [0 for _ in range(N+1)]
visited[1] = 1
queue = deque([(1,0)])

def bfs():

    while queue:
        v1, f = queue.popleft()
        cnt = 0
        for v2 in graph[v1]:
            # if visited[v2]:
            #     continue

            if fan[v2] == 1:
                queue.append((v2,f+1))
            else:
                queue.append((v2,f))
            visited[v2] = 1
            cnt += 1

        if not cnt and f == 0:
            return 'yes'
        
    return 'Yes'

print(bfs())