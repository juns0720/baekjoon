import sys
input = sys.stdin.readline
from collections import deque



queue = deque([])
for i in range(int(input())):
    t = input().split()
    if t[0] == "push":
        queue.append(t[1])
    elif t[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif t[0] == "size":
        print(len(queue))
    elif t[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif t[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif t[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    


