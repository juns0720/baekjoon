import sys
from collections import deque
input = sys.stdin.readline


n,m = map(int,input().split())
al = list(map(int,input().split()))
al.sort(reverse=True)
al = deque(al)
res = [0 for _ in range(m)]

# 최댓값 1번 콘센트에 넣기

i = 0
while al:
    e = al.popleft()
    if i == 0:
        res[i]+=e
        i = (i+1)%m
        continue

    res[i]+=e
    if res[i] == res[i-1]:
        i = (i+1)%m
    
        
print(res[0])

