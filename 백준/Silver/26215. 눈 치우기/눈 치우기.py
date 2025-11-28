import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []
for i in list(map(int,input().split())):
    heapq.heappush(hq,-i)

cnt = 0
while len(hq) > 1:
    n1 = -heapq.heappop(hq)
    n2 = -heapq.heappop(hq)
    cnt += n2
    heapq.heappush(hq,-(n1-n2))
    
if hq:
    cnt += (-hq[0])
if cnt > 1440:
    cnt = -1
print(cnt)