import sys
from collections import deque
input = sys.stdin.readline



A,B,N,M = map(int,input().split())
queue = deque([(N,0)])
visited = [0 for _ in range(1000001)]
while queue:
    n, cnt = queue.popleft()
    if n == M:
        break
    dx = [n*A, n*B, n+A, n-A, n+B, n-B, n+1, n-1]
    for nx in dx:
        if nx < 0 or nx > 100000 or visited[nx]:
            continue
        queue.append((nx, cnt+1))
        visited[nx] = 1
print(cnt)