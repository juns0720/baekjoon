import sys
import heapq
input = sys.stdin.readline

hp = []

for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if len(hp) == 0:
            print(0)
        else:
            print(heapq.heappop(hp))      
    else:
        heapq.heappush(hp,x)
            
            
