import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
cakes = list(map(int,input().split()))
cakes.sort(key = lambda x: (x%10, x))
res = 0
for i in range(len(cakes)):
    if cakes[i] == 10:
        res += 1
        continue
    while cakes[i] > 10 and m > 0:
        cakes[i] -= 10
        res += 1
        if cakes[i] == 10:
            res += 1
        m-=1
print(res)