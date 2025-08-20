import sys
from collections import deque
input = sys.stdin.readline

s = input().strip()
queue = deque()
res = 0
l = len(s)

for i in range(l):
    if s[i] == 'B':
        queue.append(i)

for i in range(l):
    if not queue:
        break

    if s[i] == 'C' and i > queue[0]:
        queue.popleft()
        res += 1

for i in range(l-1,-1,-1):
    if not queue:
        break

    if s[i] == 'A' and i < queue[-1]:
        queue.pop()
        res += 1
print(res)