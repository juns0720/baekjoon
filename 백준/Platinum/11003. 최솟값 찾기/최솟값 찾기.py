import sys
import heapq
input = sys.stdin.readline

N,L = map(int,input().split())
arr = list(map(int,input().split()))
hq = []
crnt = -L+1
for i in range(N):
    heapq.heappush(hq, (arr[i], i))
    while max(0,crnt) > hq[0][1]:
        heapq.heappop(hq)
    print(hq[0][0], end = ' ')
    crnt+=1