import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque(input().split() for _ in range(N))

while len(queue) > 1:
    name, num = queue.popleft()
    num = -(int(num)-1)
    queue.rotate(num)
    queue.popleft()
partner = queue.popleft()
print(partner[0])