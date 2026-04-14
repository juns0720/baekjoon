import sys
from math import ceil, sqrt
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

points = [(0, 0)]
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
points.append((10000, 10000))

T = n + 1

def fuel_needed(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dist = sqrt(dx * dx + dy * dy)
    return ceil(dist / 10)

def can_go(limit):
    q = deque()
    q.append((0, 0))

    visited = [10**9] * (n + 2)
    visited[0] = 0

    while q:
        cur, cnt = q.popleft()

        if cur == T:
            return True

        for nxt in range(n + 2):
            if nxt == cur:
                continue

            if fuel_needed(points[cur], points[nxt]) > limit:
                continue
            next_cnt = cnt if nxt == T else cnt + 1

            if next_cnt > k:
                continue

            if visited[nxt] <= next_cnt:
                continue

            visited[nxt] = next_cnt
            q.append((nxt, next_cnt))

    return False

left, right = 0, 1500
answer = right

while left <= right:
    mid = (left + right) // 2
    if can_go(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)