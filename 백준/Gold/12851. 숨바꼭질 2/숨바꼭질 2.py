import sys
import math
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())


min_cnt = math.inf
queue = deque([])
queue.append((N,0))
visited = [0 for _ in range(100001)]
visited[N] = 1
res = 0

while queue:
    x,cnt = queue.popleft()
    if x == K:
        if min_cnt > cnt:
            min_cnt = cnt
            res = 1
        elif min_cnt == cnt:
            res+=1
        continue
    dx = [x-1,x+1,2*x]
    for nx in dx:
        if -1 < nx < 100001 and (not visited[nx] or visited[nx] == visited[x]+1):
            queue.append((nx,cnt+1))
            visited[nx] = visited[x]+1
print(min_cnt)
print(res)