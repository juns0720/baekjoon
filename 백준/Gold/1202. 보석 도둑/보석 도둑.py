import sys 
import heapq as hq 
input = sys.stdin.readline

n,k = map(int,input().split())

jewels = sorted([list(map(int,input().split())) for _ in range(n)])
bags = sorted([int(input()) for _ in range(k)])
res = 0
tmp_jewels = []

for bag in bags:
    while jewels and jewels[0][0] <= bag:
        value = -hq.heappop(jewels)[1]
        hq.heappush(tmp_jewels,value)
    if tmp_jewels:
        res += -hq.heappop(tmp_jewels)
print(res)