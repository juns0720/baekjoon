import sys
import heapq
input = sys.stdin.readline

N, K = map(int,input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()

hq = []
sec = 1
for i in range(1,N):
    heapq.heappush(hq,-(arr[i]-arr[i-1]))

K -= 1
while hq:
    s = -heapq.heappop(hq)
    if K > 0:
        sec += 1
        K -= 1
    else:
        sec += s

print(sec)