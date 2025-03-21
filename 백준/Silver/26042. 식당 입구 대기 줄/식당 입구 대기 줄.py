import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

max_res = 0
student = n+1
queue = deque([])
for i in range(n):
    q = list(map(int,input().split()))
    if q[0] == 1:
        queue.append(q[1])
    
        if len(queue) == max_res:
            student = min(queue[-1],student)
        elif len(queue) > max_res:
            student = queue[-1]
            max_res = len(queue)
    if q[0] == 2:
        queue.popleft()
print(max_res, student)