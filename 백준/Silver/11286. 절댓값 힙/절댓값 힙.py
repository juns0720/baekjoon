import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
res = []
for i in range(N):
    tmp = int(input())
    p = 1
    if tmp == 0:
        if not heap:
            print(0)
        else:
            (n,sym) = heapq.heappop(heap)
            if sym == 0:
                print(-n)
            else:
                print(n)
    else:
        if tmp < 0:
            p = 0
        heapq.heappush(heap,(abs(tmp),p))