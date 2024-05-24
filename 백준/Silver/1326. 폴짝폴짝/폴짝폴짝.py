import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
bridge = list(map(int,input().split()))
s,e = map(int,input().split())

queue = deque([])
queue.append((s,0))
res = -1
while queue:
    x,cnt = queue.popleft()
    if x == e:
        res = cnt
        break

    for i in range(1,n):
        num = x-bridge[x-1]*i
        if num >= 1:
            queue.append((num,cnt+1))
        else:
            break

    for i in range(1,n):
        num = x+bridge[x-1]*i
        if num <= n:
            queue.append((num,cnt+1))
        else:
            break
print(res)

