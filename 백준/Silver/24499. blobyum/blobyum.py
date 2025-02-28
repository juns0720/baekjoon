import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
queue = deque(list(map(int,input().split())))
select = deque([])
total = 0
res = 0
if n == k:
    print(sum(queue))
    exit()
for i in range(n+k):
    pie = queue.popleft()
    if len(select) < k:
        select.append(pie)
        total += pie
    else:
        crnt = select.popleft()
        total -= crnt
        queue.append(crnt)
        select.append(pie)
        total += pie
    
    if len(select) == k:
        res = max(total, res) 
print(res)