import sys
from collections import deque
import heapq
input = sys.stdin.readline

N,M = map(int,input().split())
want = [[] for _ in range(200001)]
for i in range(0,N):
    temp = list(map(int,input().split()))
    for j in range(1,len(temp)):
        heapq.heappush(want[temp[j]],i)
sushi = deque(list(map(int,input().split())))
cnt = [0 for _ in range(N)]
for _ in range(M):
    n_sushi = sushi.popleft()
    if len(want[n_sushi]) != 0:
        num = heapq.heappop(want[n_sushi])
        cnt[num]+=1
for i in cnt:
    print(i,end=' ')