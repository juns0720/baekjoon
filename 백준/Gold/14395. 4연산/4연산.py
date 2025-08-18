import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while queue:
        v,c = queue.popleft()

        if v == t:
            return
        
        for nv,sym in [(v**2,'*'), (v-v,'-'), (v*2,'+'), (v//v,"/")]:
            if nv in visited or nv > MAX_SIZE or nv < 1:
                continue
            visited[nv] = visited[v] + sym
            queue.append((nv,c+1))

s,t = map(int,input().split())
if s == t:
    print(0)
    exit()
MAX_SIZE = max(s,t)
queue = deque([(s,0)])

visited = {s : ''}
bfs()

if t not in visited:
    print(-1)
else:
    print(visited[t])