import sys
from collections import deque
input = sys.stdin.readline

s1 = input().strip()
m = s1[:2]
s = int(s1[3:]) + 60 * int(m)
cnt = 0

queue = deque()
visited = [0 for _ in range(s+1)]
def bfs():
    while queue:
        sec,cnt = queue.popleft()
        if sec <= 0:
            return cnt
        for bnt in [600,60,30,10,sec]:
            if sec >= bnt:
                sec -= bnt
                if visited[sec]:
                    break
                visited[sec] = 1
                queue.append((sec,cnt+1))
                break

if s >= 30:
    queue.append((s-30,1))
    visited[s-30] = 1
queue.append((s,1))
visited[s] = 1

print(bfs())