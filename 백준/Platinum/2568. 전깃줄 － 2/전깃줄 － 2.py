import bisect
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

lines = []
for _ in range(n):
    lines.append(list(map(int,input().split())))
lines.sort(key = lambda x: x[0])


res = []
idx = []
for s,e in lines:
    t = bisect.bisect_left(res,e)
    if t == len(res):
        res.append(e)
    else:
        res[t] = e
    idx.append(t)

cnt = len(res)-1
queue = deque()
for i in range(len(idx)-1, -1, -1):
    if idx[i] == cnt:
        cnt -= 1
    else:
        queue.appendleft(lines[i])

print(len(lines)-len(res))
for i in queue:
    print(i[0])

