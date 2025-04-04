import sys
from collections import deque
input = sys.stdin.readline

queue = deque(list(map(int,str(input().strip()))))

num = 0
while queue:
    num+=1
    tmp = list(map(int,str(num)))

    for i in tmp:
        if not queue:
            break
        if queue[0] == i:
            queue.popleft()

print(num)