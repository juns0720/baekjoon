import sys
from collections import deque
input = sys.stdin.readline

N,R = map(int,input().split())

graph = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b,d = map(int,input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))

visited = [0 for _ in range(N+1)]

def find_giga():
    while queue:
        v1,c = queue.popleft()
        visited[v1] = 1
        cnt = 0
        for v2,curr_c in graph[v1]:
            if visited[v2]:
                continue
            cnt += 1
            queue.append((v2,c+curr_c))
            
        if cnt > 1:
            return v1,c
    return v1, c

queue = deque([(R,0)])
gv,gv_c = find_giga()

queue = deque([(gv,0)])

def bfs():
    res = 0
    while queue:
        v1,c = queue.popleft()

        cnt = 0
        for v2,curr_c in graph[v1]:
            if visited[v2]:
                continue
            cnt += 1
            queue.append((v2,c+curr_c))
            visited[v2] = 1
        if not cnt:
            res = max(res,c)
    return res

print(gv_c,bfs())