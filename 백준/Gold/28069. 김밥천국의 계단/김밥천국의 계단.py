import sys
from collections import deque
input = sys.stdin.readline
MAX_SIZE = 10**6
n,k = map(int,input().split())

def bfs():
    queue = deque([(0,0)])
    visited = [0 for _ in range(n+1)]
    visited[0] = 1

    while queue:
        i,cnt = queue.popleft()
        if i == n:
            return "minigimbob"
        if cnt == k:
            continue
        for ni in [i+1,i+(i//2)]:
            if ni > n or visited[ni]:
                continue
            queue.append((ni, cnt+1))
            visited[ni] = 1
    return "water"

print(bfs())