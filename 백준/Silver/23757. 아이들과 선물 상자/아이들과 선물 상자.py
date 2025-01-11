import sys
import heapq
input = sys.stdin.readline

def max_heap(arr):
    hq = []
    for i in arr:
        heapq.heappush(hq,-i)
    return hq


N,M = map(int,input().split())
gifts = max_heap(list(map(int,input().split())))    
wants = list(map(int,input().split()))


for want in wants:
    gift = -heapq.heappop(gifts)
    if gift < want:
        print(0)
        exit()
    gift -= want
    heapq.heappush(gifts,-gift)
print(1)