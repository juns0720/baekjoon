import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input())

for i in range(N):
    temp = int(input())
    if temp == 0:
        if not heap:
            print(0)
        else:
            print(abs(heapq.heappop((heap))))
    else:
        heapq.heappush(heap,-temp)

