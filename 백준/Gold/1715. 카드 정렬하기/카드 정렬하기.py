import sys
import heapq
input = sys.stdin.readline

n = int(input())
hq = [int(input()) for _ in range(n)]
heapq.heapify(hq)

res = 0
while len(hq) > 1:
    cnt = heapq.heappop(hq) + heapq.heappop(hq)
    res += cnt
    heapq.heappush(hq, cnt)

print(res)